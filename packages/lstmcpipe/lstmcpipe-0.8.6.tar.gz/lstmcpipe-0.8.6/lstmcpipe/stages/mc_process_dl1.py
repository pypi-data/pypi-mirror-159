#!/usr/bin/env python

# Code to reduce R0 data to DL1 onsite (La Palma cluster)

import shutil
import logging
from pathlib import Path
from ..utils import save_log_to_file, SbatchLstMCStage
from ..io.data_management import check_data_path, get_input_filelist

log = logging.getLogger(__name__)


def batch_process_dl1(
    dict_paths,
    conf_file,
    batch_config,
    logs,
    workflow_kind="lstchain",
    new_production=True,
):
    """
    Batch the dl1 processing jobs by particle type.

    Parameters
    ----------
    dict_paths : dict
        Core dictionary with {stage: PATHS} information
    conf_file : str
        Path to a configuration file. If none is given, a standard configuration is applied
    batch_config : dict
        Dict with source environment (to select the desired conda environment to run the r0/1_to_dl1 stage),
        and the slurm user account.
    workflow_kind: str
        One of the supported pipelines. Defines the command to be run on r0 files
    new_production: bool
        Whether to analysis simtel or reprocess existing dl1 files.
    logs: dict
        Dictionary con logs files

    Returns
    -------
    jobids_dl1_processing_stage : str
        string, separated by commas, containing all the jobids of this stage
    """
    log_process_dl1 = {}
    debug_log = {}
    jobids_dl1_processing_stage = []

    log.info("==== START {} dl1 processing ====".format(workflow_kind))

    if new_production:

        for paths in dict_paths["r0_to_dl1"]:

            try:
                check_data_path(paths["input"], glob="*.simtel.gz")
            except ValueError:
                debug_log["**EMPTY_R0_DIR**"] = f'{paths["input"]} directory does not contain any simtel.gz file'
                continue

            job_logs, jobid = r0_to_dl1(
                paths["input"],
                paths["output"],
                config_file=conf_file,
                batch_config=batch_config,
                workflow_kind=workflow_kind,
                slurm_options=paths.get("slurm_options", None),
            )
            log_process_dl1.update(job_logs)
            jobids_dl1_processing_stage.append(jobid)
            debug_log[jobid] = f'r0_dl1 job from input dir: {paths["input"]}'

    else:

        for paths in dict_paths["dl1ab"]:
            job_logs, jobid = reprocess_dl1(
                paths["input"],
                paths["output"],
                config_file=conf_file,
                batch_config=batch_config,
                workflow_kind=workflow_kind,
                slurm_options=paths.get("slurm_options", None),
            )

            log_process_dl1.update(job_logs)
            jobids_dl1_processing_stage.append(jobid)
            debug_log[jobid] = f'dl1ab job from input dir: {paths["input"]}'

    # Create a string to be directly passed
    jobids_dl1_processing_stage = ",".join(jobids_dl1_processing_stage)

    save_log_to_file(log_process_dl1, logs["log_file"], "r0_to_dl1")
    save_log_to_file(debug_log, logs["debug_file"], workflow_step="r0_to_dl1")

    log.info("==== END {} dl1 processing ====".format(workflow_kind))

    return jobids_dl1_processing_stage


def r0_to_dl1(
    input_dir,
    output_dir,
    workflow_kind="lstchain",
    config_file=None,
    batch_config=None,
    debug_mode=False,
    keep_rta_file=False,
    slurm_options=None,
):
    """
    R0 to DL1 MC onsite conversion.
    Organizes files and launches slurm jobs in two slurm arrays.


    Parameters
    ----------
    input_dir : str or Path
        path to the files directory to analyse
    output_dir : str or Path
        Output path to store files
    config_file : str or Path
        Path to the {lstchain, ctapipe, HiPeRTA} configuration file
    batch_config : dict
        Dictionary containing the full (source + env) source_environment and the slurm_account strings.
        ! NOTE : train_pipe AND dl1_to_dl2 **MUST** be run with the same environment.
    workflow_kind: str
        One of the supported pipelines. Defines the command to be run on r0 files
    slurm_options: str
        Extra slurm options to be passed

    # HIPERTA ARGUMENTS
    keep_rta_file : bool
        Flag to indicate whether to keep (keep_rta_file = True) or remove (keep_rta_file = Flase ) the
        `dl1v06_reorganized_*.h5` output file (hiperta_r0_dl1 and re-organiser stages).
        Argument to be passed to the hiperta_r0_to_dl1lstchain script.
    debug_mode : bool
        Flag to activate debug_mode. Only compatible with `hiperta` workflow kind, i.e.,
        HiPeRTA functionality. DEFAULT=False.

    Returns
    -------
    jobid2log : dict
        dictionary log containing {jobid: batch_cmd} information
    jobids_r0_dl1
        A list of all the jobs sent for input dir
    """

    log.info("\nStarting R0 to DL1 processing for files in dir : {}".format(input_dir))

    if workflow_kind == "lstchain":
        base_cmd = f"lstmcpipe_lst_core_r0_dl1 -c {config_file} "
        jobtype_id = "LST"
    elif workflow_kind == "ctapipe":
        base_cmd = f"lstmcpipe_cta_core_r0_dl1 -c {config_file} "
        jobtype_id = "CTA"
    elif workflow_kind == "hiperta":
        base_cmd = f"lstmcpipe_rta_core_r0_dl1 -c {config_file} "
        if keep_rta_file:
            base_cmd += " --keep_rta_file"
        if debug_mode:
            base_cmd += " --debug_mode"

        jobtype_id = "RTA"
    else:
        base_cmd = ''
        jobtype_id = ''
        log.critical("Please, select an allowed workflow kind.")
        exit(-1)

    raw_files_list = get_input_filelist(input_dir, glob_pattern="*.simtel.gz")

    if len(raw_files_list) < 50:
        dl1_files_per_job = 20
    else:
        dl1_files_per_job = 50

    with open("r0_to_dl1.list", "w+") as newfile:
        for f in raw_files_list:
            newfile.write(f)
            newfile.write("\n")

    log.info("{} raw R0 files".format(len(raw_files_list)))

    # If file exists, means that prod is being re-run
    output_dir = Path(output_dir)
    if output_dir.exists() and any(output_dir.iterdir()):
        shutil.rmtree(output_dir)

    job_logs_dir = output_dir.joinpath("job_logs_r0dl1")
    Path(job_logs_dir).mkdir(exist_ok=True, parents=True)

    log.info("DL1 DATA DIR: {}".format(output_dir))

    jobid2log, jobids_r0_dl1 = submit_dl1_jobs(
        input_dir,
        output_dir,
        base_cmd=base_cmd,
        file_list=raw_files_list,
        job_type_id=jobtype_id,
        dl1_files_per_batched_job=dl1_files_per_job,
        job_logs_dir=job_logs_dir,
        batch_config=batch_config,
        dl1_processing_type="r0_to_dl1",
        slurm_options=slurm_options,
    )

    # copy config into working dir
    if config_file is not None:
        shutil.copyfile(config_file, job_logs_dir.joinpath(Path(config_file).name))

    # save file lists into logs
    shutil.move("r0_to_dl1.list", job_logs_dir)

    # return it log dictionary
    return jobid2log, jobids_r0_dl1


def reprocess_dl1(
    input_dir,
    output_dir,
    workflow_kind="lstchain",
    config_file=None,
    batch_config=None,
    dl1_files_per_job=50,
    slurm_options=None,
):
    """
    Reprocessing of existing dl1 files.
    Organizes files and launches slurm jobs in two slurm arrays.
    The same train/test split performed with the earlier r0 to dl1
    processing is used.

    Parameters
    ----------
    input_dir : str
        path to the files directory to analyse
    output_dir : str or Path
        Output path to store files
    config_file :str
        Path to a configuration file. If none is given, the standard configuration of the selected pipeline is applied
    batch_config : dict
        Dictionary containing the (full) source_environment and the slurm_account strings.
        ! NOTE : train_pipe AND dl1_to_dl2 **MUST** be run with the same environment.
    workflow_kind: str
        One of the supported pipelines. Defines the command to be run on r0 files
    dl1_files_per_job: int
        Number of dl1 files to be processed per job array that was batched.
    slurm_options: str
        Extra slurm options to be passed to the sbatch command

    Returns
    -------
    jobid2log : dict
        dictionary log containing {jobid: batch_cmd} information
    jobids_dl1_dl1
        A list of all the jobs sent for input dir
    """
    log.info("Applying DL1ab on DL1 files in {}".format(input_dir))

    if workflow_kind == "lstchain":
        base_cmd = f"lstmcpipe_lst_core_dl1ab -c {config_file} "
        jobtype_id = "LST"
    elif workflow_kind == "ctapipe":
        base_cmd = f"lstmcpipe_cta_core_r0_dl1 -c {config_file} "
        jobtype_id = "CTA"
    else:
        base_cmd = ""
        jobtype_id = ""
        log.critical(f"Unknown workflow {workflow_kind}")
        exit(-1)

    check_data_path(input_dir)
    dl1ab_filelist = [file.resolve().as_posix() for file in Path(input_dir).glob("*.h5")]

    log.info("{} DL1 files".format(len(dl1ab_filelist)))

    with open("dl1ab.list", "w+") as newfile:
        for f in dl1ab_filelist:
            newfile.write(f)
            newfile.write("\n")

    Path(output_dir).mkdir(exist_ok=True, parents=True)
    job_logs_dir = Path(output_dir).joinpath("job_logs_dl1ab")
    Path(job_logs_dir).mkdir(exist_ok=True)

    log.info("DL1ab destination DATA DIR: {}".format(output_dir))

    jobid2log, jobids_dl1_dl1 = submit_dl1_jobs(
        input_dir,
        output_dir,
        base_cmd=base_cmd,
        file_list=dl1ab_filelist,
        job_type_id=jobtype_id,
        dl1_files_per_batched_job=dl1_files_per_job,
        job_logs_dir=job_logs_dir,
        batch_config=batch_config,
        dl1_processing_type="dl1ab",
        slurm_options=slurm_options,
    )

    # copy config into working dir
    if config_file is not None:
        shutil.copyfile(config_file, job_logs_dir.joinpath(Path(config_file).name))

    # save file lists into logs
    shutil.move("dl1ab.list", job_logs_dir)

    # return it log dictionary
    return jobid2log, jobids_dl1_dl1


def submit_dl1_jobs(
    input_dir,
    output_dir,
    base_cmd,
    file_list,
    job_type_id,
    dl1_files_per_batched_job,
    job_logs_dir,
    batch_config,
    n_jobs_parallel=100,
    dl1_processing_type="r0_to_dl1",
    slurm_options="",
):
    """
    Compose sbatch command and batches it

    Parameters
    ----------
    input_dir: str
        path to the files directory to analyse
    output_dir: str
        Output path to store files
    base_cmd: str
        command choosing the lstmcpipe core script type (script_batch_filelist_*)
    file_list: list
        list of r0_dl1 or dl1ab filelist to be passed to the core script
    job_type_id: str
        String for job naming depending on the workflow
    dl1_files_per_batched_job: int
        Number of dl1 files to be processed per job array that was batched.
    job_logs_dir: Path
        Directory for the logs of the core script output.
        Should be Path(output_dir).joinpath("job_logs_*")
    batch_config: dict
        Dictionary containing the full (source + env) source_environment and the slurm_account strings.
        ! NOTE : train_pipe AND dl1_to_dl2 **MUST** be run with the same environment.
    n_jobs_parallel: int
        Number of array jobs to be processed in parallel.
        Default = 100
    dl1_processing_type: str
        String for job and filelist naming
    slurm_options: str
        Extra slurm options to be passed

    Returns
    -------
    jobid2log: dict
    jobid: str

    """
    jobid2log = {}

    number_of_sublists = len(file_list) // dl1_files_per_batched_job + int(
        len(file_list) % dl1_files_per_batched_job > 0
    )

    for i in range(number_of_sublists):
        output_file = job_logs_dir.joinpath("{}_{}.sublist".format(dl1_processing_type, i)).resolve().as_posix()
        with open(output_file, "w+") as out:
            for line in file_list[i * dl1_files_per_batched_job : dl1_files_per_batched_job * (i + 1)]:  # noqa
                out.write(line)
                out.write("\n")

    log.info(f"{number_of_sublists} files generated for list of files at {input_dir}")

    sublist_names = [f.as_posix() for f in Path(job_logs_dir).glob("*.sublist")]  # Number of sublists ??

    # start 1 jobarray with all files included. The job selects its file based on its task id
    cmd = f'{base_cmd} -f {" ".join(sublist_names)} --output_dir {output_dir}'

    sbatch_process_dl1 = SbatchLstMCStage(
        dl1_processing_type,
        wrap_command=cmd,
        slurm_error=job_logs_dir.joinpath("job_%A_%a.e").as_posix(),
        slurm_output=job_logs_dir.joinpath("job_%A_%a.o").as_posix(),
        slurm_account=batch_config["slurm_account"],
        source_environment=batch_config["source_environment"],
    )
    if dl1_processing_type == "r0_to_dl1":
        sbatch_process_dl1.r0_dl1_options(
            process_dl1_job_name=f"{job_type_id}-{dl1_processing_type}",
            array=f"0-{len(sublist_names) - 1}%{n_jobs_parallel}",
            partition="long",
            extra_slurm_options="",
        )
    elif dl1_processing_type == "dl1ab":
        sbatch_process_dl1.dl1ab_options(
            process_dl1ab_job_name=f"{job_type_id}-{dl1_processing_type}",
            array=f"0-{len(sublist_names) - 1}%{n_jobs_parallel}",
            partition="long",
            extra_slurm_options="",
        )

    jobid = sbatch_process_dl1.submit()
    log.debug(f"Submitted batch job {jobid}")

    jobid2log.update({jobid: sbatch_process_dl1.slurm_command})

    return jobid2log, jobid

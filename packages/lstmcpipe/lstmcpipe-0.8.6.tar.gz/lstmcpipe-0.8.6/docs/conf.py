# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


import os
import sys
import json
import datetime

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

with open(os.path.join(os.path.dirname(__file__), "..", "codemeta.json")) as file:
    metadata = json.load(file)

# General information about the project.
project = metadata["name"]
author = ""
for aut in metadata["author"]:
    author += f"{aut['givenName']} {aut['familyName']},"

copyright = "{}.  Last updated {}".format(author, datetime.datetime.now().strftime("%d %b %Y %H:%M"))

# The full version, including alpha/beta/rc tags
release = metadata['version']

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_automodapi.automodapi",
    "sphinxarg.ext",
    "sphinx.ext.napoleon",
    "sphinxcontrib.mermaid",
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

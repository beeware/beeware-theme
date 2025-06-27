# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import beeware_theme


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BeeWare Theme'
copyright = '2025, BeeWare Project'
author = 'BeeWare Project'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_tabs.tabs",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = "images/brutus-270.png"

html_theme = 'furo'
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_context = {}
html_theme_options = {}

beeware_theme.init(
    project_name="beeware-theme",
    templates=templates_path,
    context=html_context,
    static=html_static_path,
    css=html_css_files,
    theme_options=html_theme_options,
)

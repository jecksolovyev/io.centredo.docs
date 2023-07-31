# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_bootstrap_theme

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'WhiteDoc'
copyright = '2023, DocStudio'
author = 'DocStudio'

# The full version, including alpha/beta/rc tags
release = '1.27'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.redoc',
    # 'rst2pdf.pdfbuilder'
]
# pdf_documents = [('index', u'Centredo manual', u'Centredo documentation', u'Centredo')]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

latex_engine = 'xelatex'

# def setup(app):
#     app.add_stylesheet('theme_overrides.css')
#     app.add_javascript('ultra_custom.js')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

master_doc = 'index'

redoc_uri = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'
redoc = [
    {
        'name': 'Open API',
        'page': 'pages/apiIntegration/openapi/openApi',
        'spec': 'pages/apiIntegration/openapi/swagger.json',
        'embed': True,
        'opts': {
            'suppress-warnings' : True,
            'lazy-rendering' : False,
            'required-props-first' : True,
            'hide-hostname' : True
        }
    }
]

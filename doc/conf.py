#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2019 TeNPy Developers, GNU GPLv3
#
# tenpy documentation build configuration file, created by
# sphinx-quickstart on Mon Feb 18 00:04:33 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if not sys.version_info >= (3, 5):
    print("ERROR: old python version, called by python version\n" + sys.version)
    sys.exit(1)

try:
    import tenpy.version
except:
    print("ERROR: can't import tenpy.")
    sys.exit(1)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '2.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'numpydoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['sphinx_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'TeNPy'
copyright = '2016-2019, TeNPy Developers'
author = 'TeNPy Developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = tenpy.__version__
# The full version, including alpha/beta/rc tags.
release = tenpy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['sphinx_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# default options for autodoc
autodoc_default_options = {
    #  'inherited-members': True,  # inherit methods and attributes from base classes
    #  'special-members': '__init__',
}
autodoc_member_order = 'bysource'

# Avoid a bunch of warnings when using properties with doc strings in classes.
# see https://github.com/phn/pytpm/issues/3#issuecomment-12133978
numpydoc_show_class_members = True
numpydoc_show_inherited_class_members = True
numpydoc_class_members_toctree = False
# if you get a lot of warnings like::
# None:None: WARNING: toctree contains reference to nonexisting document u'reference/tenpy.linalg.charges.LegCharge.get_qindex'
# then try to update your numpydoc package with
# > pip install --upgrade numpydoc

autosummary_generate = True

# -- Options for output of To-Do admonitions in doc-strings

# show todo-boxes in output
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "images/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs. This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "images/logo.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []  # ['sphinx_static']   # not needed

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {
    '**': ['localtoc.html', 'relations.html', 'searchbox.html', 'globaltoc.html'],
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'tenpydoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'tenpy.tex', 'tenpy Documentation', 'TenPy Team', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'tenpy', 'tenpy Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'TeNPy', 'TeNPy Documentation', 'TeNPy community', 'TeNPy',
     'One line description of project.', 'Miscellaneous'),
]

# cross links to other sphinx documentations
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('https://matplotlib.org', None),
}

# extlinks
extlinks = {
    'arxiv': ('https://arxiv.org/abs/%s', 'arXiv:'),
    'doi': ('https://dx.doi.org/%s', 'doi:'),
    'issue': ('https://github.com/tenpy/tenpy/issues/%s', 'issue #'),
    'forum': ('https://tenpy.johannes-hauschild.de/viewtopic.php?t=%s', 'Community forum topic ')
}

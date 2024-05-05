import datetime
import doctest
import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("./.."))

import pywlk

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "nbsphinx",
    "nbsphinx_link",
]

autosummary_generate = True
templates_path = ["_templates"]
exclude_patterns = ["_build", "_templates"]

source_suffix = ".rst"
master_doc = "index"

author = "Roman Joeres"
project = "PyWLK"
copyright = f"{datetime.datetime.now().year}, {author}"

version = list(open("../pyproject.toml", "r").readlines())[2].strip().split("\"")[1].split("\"")[0]
release = version

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

doctest_default_flags = doctest.NORMALIZE_WHITESPACE
autodoc_member_order = "bysource"
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("http://docs.scipy.org/doc/numpy", None),
}

html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "logo_only": True,
    "navigation_depth": 2,
}

rst_context = {"pywlk": pywlk}

add_module_names = False
fail_on_warning = True
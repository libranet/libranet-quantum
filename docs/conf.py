"""Sphinx configuration."""
project = "libranet-qiskit"
author = "Wouter Vanden Hove"
copyright = "2023, Wouter Vanden Hove"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"

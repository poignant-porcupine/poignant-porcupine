# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "poignant-porcupine"
copyright = "2026, Adam Carter"
author = "Adam Carter"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

intersphinx_mapping = {
    "poignant-porcupine": (
        "https://poignant-porcupine.readthedocs.io/en/latest/",
        None,
    ),
    "poignant-porcupine-core": (
        "https://poignant-porcupine.readthedocs.io/projects/poignant-porcupine-core/en/latest/",
        None,
    ),
    "poignant-porcupine-domain": (
        "https://poignant-porcupine.readthedocs.io/projects/poignant-porcupine-domain/en/latest/",
        None,
    ),
}

intersphinx_disabled_reftypes = ["*"]

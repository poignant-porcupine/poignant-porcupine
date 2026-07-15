# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "poignant-porcupine-core"
copyright = "2026, Adam Carter"
author = "Adam Carter"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
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

if os.environ.get("READTHEDOCS") == "True":
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT / "src"))

    PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
    PACKAGE_ROOT = PROJECT_ROOT / "libs" / "poignant-porcupine-core" / "src" / "poignant_porcupine_core"

    def run_apidoc(_):
        from sphinx.ext import apidoc

        apidoc.main(
            [
                "--force",
                "--implicit-namespaces",
                "--module-first",
                "--separate",
                "-o",
                str(PROJECT_ROOT / "libs" / "poignant-porcupine-core" / "docs" / "reference"),
                str(PACKAGE_ROOT),
            ]
        )

    def setup(app):
        app.connect("builder-inited", run_apidoc)

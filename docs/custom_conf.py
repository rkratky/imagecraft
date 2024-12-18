import os
import datetime
import pathlib

import craft_parts_docs

from gen_cli_docs import gen_docs

# Custom configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# The file is included in the common conf.py configuration file.
# You can modify any of the settings below or add any configuration that
# is not covered by the common conf.py file.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# If you're not familiar with Sphinx and don't want to use advanced
# features, it is sufficient to update the settings in the "Project
# information" section.

############################################################
### Project information
############################################################

# Product name
project = "Imagecraft"
author = "Canonical Ltd."

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = project + " documentation"

# The default value uses the current year as the copyright year.
#
# For static works, it is common to provide the year of first publication.
# Another option is to give the first year and the current year
# for documentation that is often changed, e.g. 2022–2023 (note the en-dash).
#
# A way to check a GitHub repo's creation date is to obtain a classic GitHub
# token with 'repo' permissions here: https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the GitHub API's output:
#
# curl -H 'Authorization: token <TOKEN>' \
#   -H 'Accept: application/vnd.github.v3.raw' \
#   https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = "%s, %s" % (datetime.date.today().year, author)

## Open Graph configuration - defines what is displayed as a link preview
## when linking to the documentation from another website (see https://ogp.me/)
# The URL where the documentation will be hosted (leave empty if you
# don't know yet)
# NOTE: If no ogp_* variable is defined (e.g. if you remove this section) the
# sphinxext.opengraph extension will be disabled.
ogp_site_url = "https://canonical-imagecraft.readthedocs-hosted.com/"
# The documentation website name (usually the same as the product name)
ogp_site_name = project
# The URL of an image or logo that is used in the preview
ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"

# Update with the local path to the favicon for your product
# (default is the circle of friends)
html_favicon = ".sphinx/_static/favicon.png"

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {
    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    "product_page": "documentation.ubuntu.com",
    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    "product_tag": "_static/tag.png",
    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    "discourse": "https://discourse.ubuntu.com/c/foundations/",
    # Change to the Mattermost channel you want to link to
    # (use an empty value if you don't want to link)
    "mattermost": "https://chat.canonical.com/canonical/channels/documentation",
    # Change to the GitHub URL for your project
    "github_url": "https://github.com/canonical/imagecraft",
    # Change to the branch for this version of the documentation
    "github_version": "main",
    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    "github_folder": "/docs/",
    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    "github_issues": "enabled",
    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "none",
}

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
slug: str = ""

############################################################
### Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',
# You can also configure redirects in the Read the Docs project dashboard
# (see https://docs.readthedocs.io/en/stable/guides/redirects.html).
# NOTE: If this variable is not defined, set to None, or the dictionary is empty,
# the sphinx_reredirects extension will be disabled.
redirects: dict[str, str] = {}

############################################################
### Link checker exceptions
############################################################

# Links to ignore when checking links
linkcheck_ignore = ["http://127.0.0.1:8000", "https://apt-repo.com"]

# Pages on which to ignore anchors
# (This list will be appended to linkcheck_anchors_ignore_for_url)
custom_linkcheck_anchors_ignore_for_url: list[str] = []

############################################################
### Additions to default configuration
############################################################

## The following settings are appended to the default configuration.
## Use them to extend the default functionality.
# NOTE: Remove this variable to disable the MyST parser extensions.
custom_myst_extensions: list[str] = []

# Add custom Sphinx extensions as needed.
# This array contains recommended extensions that should be used.
# NOTE: The following extensions are handled automatically and do
# not need to be added here: myst_parser, sphinx_copybutton, sphinx_design,
# sphinx_reredirects, sphinxcontrib.jquery, sphinxext.opengraph
custom_extensions = [
    "sphinx_tabs.tabs",
    "sphinx.ext.ifconfig",
    "canonical.youtube-links",
    "canonical.related-links",
    "canonical.custom-rst-roles",
    "canonical.terminal-output",
    "notfound.extension",
    "sphinxcontrib.details.directive",
]

# Add custom required Python modules that must be added to the
# .sphinx/requirements.txt file.
# NOTE: The following modules are handled automatically and do not need to be
# added here: canonical-sphinx-extensions, furo, linkify-it-py, myst-parser,
# pyspelling, sphinx, sphinx-autobuild, sphinx-copybutton, sphinx-design,
# sphinx-notfound-page, sphinx-reredirects, sphinx-tabs, sphinxcontrib-jquery,
# sphinxext-opengraph
custom_required_modules: list[str] = [
    "craft-parts==2.1.1",
    "craft-application==4.2.5",
    "sphinxcontrib-details-directive==0.1.0",
]

# Add files or directories that should be excluded from processing.
custom_excludes = [
    "doc-cheat-sheet*",
    # Excluded here because they are either included explicitly in other
    # documents (so they generate "duplicate label" errors) or they aren't
    # used in this documentation at all (so they generate "unreferenced"
    # errors).
    "common/craft-parts/explanation/parts.rst",
    "common/craft-parts/explanation/overlay_parameters.rst",
    "common/craft-parts/explanation/overlays.rst",
    "common/craft-parts/explanation/how_parts_are_built.rst",
    "common/craft-parts/explanation/overlay_step.rst",
    "common/craft-parts/explanation/dump_plugin.rst",
    "common/craft-parts/how-to/craftctl.rst",
    "common/craft-parts/how-to/include_files.rst",
    "common/craft-parts/how-to/override_build.rst",
    "common/craft-parts/reference/step_execution_environment.rst",
    "common/craft-parts/reference/step_output_directories.rst",
    "common/craft-parts/reference/parts_steps.rst",
    "common/craft-parts/reference/partition_specific_output_directory_variables.rst",
    "common/craft-parts/reference/plugins/ant_plugin.rst",
    "common/craft-parts/reference/plugins/autotools_plugin.rst",
    "common/craft-parts/reference/plugins/cmake_plugin.rst",
    "common/craft-parts/reference/plugins/dotnet_plugin.rst",
    "common/craft-parts/reference/plugins/dump_plugin.rst",
    "common/craft-parts/reference/plugins/go_plugin.rst",
    "common/craft-parts/reference/plugins/make_plugin.rst",
    "common/craft-parts/reference/plugins/maven_plugin.rst",
    "common/craft-parts/reference/plugins/meson_plugin.rst",
    "common/craft-parts/reference/plugins/nil_plugin.rst",
    "common/craft-parts/reference/plugins/npm_plugin.rst",
    "common/craft-parts/reference/plugins/python_plugin.rst",
    "common/craft-parts/reference/plugins/poetry_plugin.rst",
    "common/craft-parts/reference/plugins/qmake_plugin.rst",
    "common/craft-parts/reference/plugins/rust_plugin.rst",
    "common/craft-parts/reference/plugins/scons_plugin.rst",
]

# Add CSS files (located in .sphinx/_static/)
custom_html_css_files: list[str] = []

# Add JavaScript files (located in .sphinx/_static/)
custom_html_js_files: list[str] = []

## The following settings override the default configuration.

# Specify a reST string that is included at the end of each file.
# If commented out, use the default (which pulls the reuse/links.txt
# file into each reST file).
custom_rst_epilog = """
.. include:: /reuse/links.txt
"""

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
disable_feedback_button = False

# Add tags that you want to use for conditional inclusion of text
# (https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#tags)
custom_tags: list[str] = []

############################################################
### Additional configuration
############################################################

## Add any configuration that is not covered by the common conf.py file.

# Define a :center: role that can be used to center the content of table cells.
rst_prolog = """
.. role:: center
   :class: align-center
"""


def generate_cli_docs(nil):
    gen_docs(pathlib.Path("./"))


def setup(app):
    app.connect("builder-inited", generate_cli_docs)


# Setup libraries documentation snippets for use in imagecraft docs.
common_docs_path = pathlib.Path(__file__).parent / "common"
craft_parts_docs_path = pathlib.Path(craft_parts_docs.__file__).parent / "craft-parts"
(common_docs_path / "craft-parts").unlink(missing_ok=True)
(common_docs_path / "craft-parts").symlink_to(
    craft_parts_docs_path, target_is_directory=True
)

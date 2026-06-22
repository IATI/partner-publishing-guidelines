# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

from urllib.parse import urlparse

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Downstream Partner Publishing Guidelines"

# URL of the live tool this repo documents. None when the docs themselves
# are the deliverable (no separate tool to link).
tool_url = None

# Short label used in the nav. Defaults to ``project`` when None.
nav_label = None

# Eyebrow text: the smaller text that appears directly above the website title
eyebrow_text = "IATI Guidelines: Downstream Partners"

# GitHub repository URL (for "Edit on GitHub" links)
github_repository = "https://github.com/IATI/downstream-partner-publishing-guidelines"

# Plausible analytics domain, derived from tool_url so docs are tracked
# under the tool's site. Set to None to disable.
plausible_domain = urlparse(tool_url).hostname if tool_url else None

# Supported languages for the documentation
languages = ["en", "fr", "es"]

redoc = [
    {
        "name": "Widgets API",
        "page": "api-docs/test-widget-api",
        "spec": "specifications/test-widget-api.yaml",
        "embed": True,
        "template": "_templates/redoc-custom.j2",
    }
]

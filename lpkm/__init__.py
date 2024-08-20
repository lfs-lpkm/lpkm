import os
import json

__version__ = "0.0.1"


LIBDIR = "/usr/lib/lpkm"
PY_MODULES_LIBDIR = f"{LIBDIR}/lpkm"


# These things might change when running in some cases
LPKM_VAR_LIB = "/var/lib/lpkm/"
LPKM_REPO_LISTS_DIR = f"{LPKM_VAR_LIB}/lists" # Contains links for repos
LPKM_RELEASE_SOURCES_DIR = f"{LPKM_VAR_LIB}/sources" # Stores release files downloaded from repos

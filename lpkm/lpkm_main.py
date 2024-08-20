import os
import json

import lpkm
from lpkm import cmd_args


def write_default_list():
    default_lists_data = {"default": "http://localhost:9080/"}

    with open(f"{lpkm.LPKM_REPO_LISTS_DIR}/list", "w+") as list_file:
        json.dump(default_lists_data, list_file, indent=4)

def initial_checks_and_fixs():
    if os.geteuid() != 0:
        print("Trying running with root permission!")
        exit(2)

    # Setting up /var/lib/lpkm
    if not os.path.exists(lpkm.LPKM_VAR_LIB):
        os.mkdir(lpkm.LPKM_VAR_LIB)
    if not os.path.isdir(lpkm.LPKM_VAR_LIB):
        os.remove(lpkm.LPKM_VAR_LIB)
        os.mkdir(lpkm.LPKM_VAR_LIB)

    # /var/lib/lpkm/lists
    if not os.path.exists(lpkm.LPKM_REPO_LISTS_DIR):
        os.mkdir(lpkm.LPKM_REPO_LISTS_DIR)
        write_default_list()
    if not os.path.isdir(lpkm.LPKM_REPO_LISTS_DIR):
        os.remove(lpkm.LPKM_REPO_LISTS_DIR)
        os.mkdir(lpkm.LPKM_REPO_LISTS_DIR)
        write_default_list()
    
    # /var/lib/lpkm/sources
    if not os.path.exists(lpkm.LPKM_RELEASE_SOURCES_DIR):
        os.mkdir(lpkm.LPKM_RELEASE_SOURCES_DIR)
    if not os.path.isdir(lpkm.LPKM_RELEASE_SOURCES_DIR):
        os.remove(lpkm.LPKM_RELEASE_SOURCES_DIR)
        os.mkdir(lpkm.LPKM_RELEASE_SOURCES_DIR)
    



def main():
    initial_checks_and_fixs()

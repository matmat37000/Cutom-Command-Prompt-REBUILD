
from pathlib import Path
import os

from log import initLog, log
from keywords import OK, FAILED

PATHS_FOLDERS: dict = {
    "CONFIG_DIR": rf"{Path.home()}\.pyPrompt",
    "PLUGIN_DIR": rf"{Path.home()}\.pyPrompt\plugin",
    }
PATH_FILES: dict = {
    "PLUGIN_CONFIG_FILE": rf"{Path.home()}\.pyPrompt\settings.json",
}

def launch():
        # Run initLog before running app
        initLog()
        
        is_OK = check_folders()
        
        if is_OK: is_OK = check_files()
        if  is_OK: is_OK = read_config()
        else: default_config()
        
        return OK
        
def check_folders():
    """Check files and folders before starting up app"""
    for key, folder in PATHS_FOLDERS.items():
        if not os.path.exists(folder): 
            Path.mkdir(folder)
            log(f"DIR [{folder}] CREATED ! KEY: {key}")
    return OK

def check_files():
    """Check if config file exist"""
    failed_count = 0
    for key, folder in PATH_FILES.items():
        if not os.path.exists(folder):
            with open(folder, "x") as file:
                file.write('{}')
                log(f'FILE [{folder}] CREATED ! KEY: {key}')
                failed_count += 1
        if failed_count > 0: return FAILED
        else: return OK
        

def default_config():
    pass

def read_config():
    pass
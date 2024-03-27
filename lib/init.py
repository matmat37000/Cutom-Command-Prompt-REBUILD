
from pathlib import Path
import os

from lib.loging import Log
from lib.keywords import keywords

PATHS_FOLDERS: dict = {
    "CONFIG_DIR": rf"{Path.home()}\.pyPrompt",
    "PLUGIN_DIR": rf"{Path.home()}\.pyPrompt\plugin",
    }
PATH_FILES: dict = {
    "PLUGIN_CONFIG_FILE": rf"{Path.home()}\.pyPrompt\settings.json",
}

def launch() -> bool:
        # Run initLog before running app
        Log.init_log()
        
        methods: list = [check_folders, check_files, default_config, read_config]
        for method in methods:
            if method():
                print("Ok")
            else:
                raise "Err"
        
        return keywords.OK
        
def check_folders() -> bool:
    """Check files and folders before starting up app"""
    for key, folder in PATHS_FOLDERS.items():
        if not os.path.exists(folder): 
            Path.mkdir(folder)
            Log.log(f"DIR [{folder}] CREATED ! KEY: {key}")
    return keywords.OK

def check_files() -> bool:
    """Check if config file exist"""
    failed_count = 0
    for key, folder in PATH_FILES.items():
        if not os.path.exists(folder):
            with open(folder, "x") as file:
                file.write('{}')
                Log.log(f'FILE [{folder}] CREATED ! KEY: {key}')
                failed_count += 1
        if failed_count > 0: return keywords.FAILED
        else: return keywords.OK 

def default_config() -> bool:
    return True

def read_config() -> bool:
    return True
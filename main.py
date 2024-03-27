
import os
from pathlib import Path

from  lib.loging import Log
from lib.keywords import keywords
from lib.init import launch

PATHS: dict = {
    "CONFIG_DIR": rf"{Path.home()}\.pyPrompt",
    }

# def init():
    # """Colection of fonction to init the project"""
    
    # # Run initLog before running app
    # Log.init_log()
    
    # # Check files and folders before starting up app
    # for key, folder in PATHS.items():
    #     if not os.path.exists(folder): 
    #         Path.mkdir(folder)
    #         Log.add_log(f"DIR [{folder}] CREATED ! KEY: {key}")
    
    
    
    # return keywords.OK  

def main(**args):
    if launch() == keywords.OK:
        print('Running')
    return

if __name__ == "__main__":
    main()
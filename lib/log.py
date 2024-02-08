
import os

LOG_PATH = rf"./logs.txt"

def initLog() -> None:
    """Create log file if he doesn't exists"""
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "xt", encoding="utf-8")as file:
            file.write("Created!")
    

def log(txt: str) -> None:
    """Write in the log file the passed text"""
    with open(LOG_PATH, "a", encoding="utf-8") as file:
        text = f"\n{txt.strip()}"
        file.writelines(text)
        print(text)
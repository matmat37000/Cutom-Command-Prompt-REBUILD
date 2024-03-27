
import os


class Log:
    """Loging function"""
    
    def __init__(self) -> None:
        self.LOG_PATH = rf"./logs.txt"
    
    def init_log(self) -> None:
        """Create log file if he doesn't exists"""
        if not os.path.exists(self.LOG_PATH):
            with open(self.LOG_PATH, "xt", encoding="utf-8") as file:
                file.write("Created!")

    def add_log(self, txt: str) -> None:
        """Write in the log file the passed text"""
        with open(self.LOG_PATH, "a", encoding="utf-8") as file:
            text = f"\n{txt.strip()}"
            file.writelines(text)
            print(text)
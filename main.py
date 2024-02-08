
from lib.keywords import *
from lib.log import initLog, log
from lib.init import launch



def main(**args):
    if launch() == OK:
        print('Running')
        
    return

if __name__ == "__main__":
    main()
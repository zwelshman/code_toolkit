import logging
from os import waitpid


DIR = "src\\util\\Logging\\"

CUSTOM_DATA = {
    "user":"zach@me.com"
}

def some_function():
    logging.debug("This is a debugger message", extra=CUSTOM_DATA)

def main():
    # set custom log level with some parameters
    

    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s "
    datestr = "%d/%m/%Y %I:%M:%S %p" 

    logging.basicConfig(filename=DIR + "/output_custom.log", 
                    level=logging.DEBUG, 
                    filemode='w',
                    format=fmtstr,
                    datefmt = datestr)
    
    #log start
    logging.info("Started process", extra=CUSTOM_DATA)
    
    #calling func
    some_function()
    
    #log end
    logging.warning("Ended process", extra=CUSTOM_DATA)

    
if __name__ == "__main__":
    
    main()
    
import functools
import time
import logging
import schedule
import getpass





DIR = "src\\util\\Scheduling\\"


# This decorator can be applied to
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        CUSTOM_DATA = {
            "username":f"{getpass.getuser()}"
            }


        fmtstr = "User:%(username)s  %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s "
        datestr = "%d/%m/%Y %I:%M:%S %p" 
        logging.basicConfig(filename=DIR + "./schedule_call.log", 
                        level=logging.DEBUG, 
                        filemode='w',
                        format=fmtstr,
                        datefmt = datestr
                        )

        logging.info(f"Started process....{func.__name__}", extra=CUSTOM_DATA)
        
        result = func(*args, **kwargs)
        
        logging.info(f"Ended process....{func.__name__}", extra=CUSTOM_DATA)
        return result
    return wrapper


def main():

    @with_logging
    def job():
        print("I'm working...")

    schedule.every(3).seconds.do(job)

    while 1:
        schedule.run_pending()
        #time.sleep(1)

if __name__ == "__main__":
    main()

import functools
import time
import logging

DIR = "main_scripts/logs"

# This decorator can be applied to
def with_logging(func):
    """ logging wrapper to apply to functions """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """ logging config """


        fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s "
        datestr = "%d/%m/%Y %I:%M:%S %p"
        logging.basicConfig(filename=DIR + "/ltht_data_load.log",
                        level=logging.DEBUG,
                        filemode='a',
                        format=fmtstr,
                        datefmt = datestr
                        )

        logging.info(f"Started process....{func.__name__}")

        result = func(*args, **kwargs)

        logging.info(f"Ended process....{func.__name__}")
        return result
    return wrapper

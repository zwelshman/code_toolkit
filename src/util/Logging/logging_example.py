# using logging api

import logging


dir = "src\\util\\Logging\\"


def main():
    # set basic log level with some parameters
    logging.basicConfig(level=logging.DEBUG, 
                    filename=dir + "/output.log",
                    filemode='w')

    logging.debug("this is a debugging")
    logging.info("this is a  info")
    logging.warning("this is a warning")
    logging.error("this is a error")
    logging.critical("this is a critial")

    string = 'string'
    number = 10
    logging.info(f'Here is a {string} variable and a {number}')

if __name__ == "__main__":
    main()

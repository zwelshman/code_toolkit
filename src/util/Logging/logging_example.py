#using logging api

import logging



def main():
    #set basic log level
    logging.basicConfig(level=logging.DEBUG, filename = "output.log")

    logging.debug('this is a debugging')

    logging.info('this is a  info')

    logging.warning('this is a warning')

    logging.error('this is a error')

    logging.critical('this is a critial')

if __name__ == "__main__":
    main()

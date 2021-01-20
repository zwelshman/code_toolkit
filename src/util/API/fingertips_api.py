import logging
import fingertips_py as ftp 

DIR = "src\\util\\API\\"

CUSTOM_DATA = {
    "user":"zach Welshman"
}

def get_df():
    df = ftp.get_data_for_indicator_at_all_available_geographies(indicator_id=92603)   
    logging.debug(f" Making API call from get_df", extra=CUSTOM_DATA)
    return df

def main():

    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s "
    datestr = "%d/%m/%Y %I:%M:%S %p" 

    logging.basicConfig(filename=DIR + "/phe_api_call.log", 
                    level=logging.DEBUG, 
                    filemode='w',
                    format=fmtstr,
                    datefmt = datestr)
    
    #log start
    logging.info("Started process....", extra=CUSTOM_DATA)
    
    #calling func
    data = get_df()
    
  
    #log end
    if len(data) == 0:
        raise AssertionError (logging.critical(f"Ended process, data retrieved 0 rows", extra=CUSTOM_DATA))
    else:
        logging.info(f"Ended process, data retrieved {len(data)} rows", extra=CUSTOM_DATA)


if __name__ == "__main__":
    main()

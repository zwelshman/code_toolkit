import pyodbc
import pandas as pd
import dask.dataframe as dd
from sqlalchemy import *
import urllib


def sqltoDF(PathToQuery, server, database):
    try:
        server = server
        database = database
        username = ""
        password = ""
        
        params = urllib.parse.quote_plus(
            "DRIVER={SQL Server};SERVER="
            + server
            + ";DATABASE="
            + database
            + ";UID="
            + username
            + ";PWD="
            + password
        )

        cnxn = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        query = open(PathToQuery)
        sqlDF = pd.read_sql_query(query.read(), cnxn)
        #sqlDF = dd.from_pandas(sqlDF1, npartitions=300)
        #sqlDF = dd.read_sql_table(query.read(), cnxn, npartitions=10, index_col="LOAD_ID")
        
    except:
        print(
            "Uh oh! Something is not right, you should check the you 1) Have access to the database 2) Are connecting to the right database 3) The query is correct 4) You are pointing to the correct Path"
        )
        raise ValueError(
            "A very specific bad thing happened, chase up the error tree to find out."
        )

    return sqlDF
   
def sqltoDF2(query, path, database, server):
    query = SQL file (query.SQL)
    path = location of SQL file
    database = database ()
    server = server ()
    
    example useage
    sqltoDF(query='query.sql',path='../../src/', database = '', server='')
    '''
    conn = create_engine(f'mssql+pyodbc://{database}/{server}?driver=SQL+Server')
    query = open(path + query)
    sqlDF = pd.read_sql_query(query.read(), conn)
    return sqlDF

#for dask use URI
server = ''
database = ''
username = ""
password = ""

params = urllib.parse.quote_plus("DRIVER={xxxx};SERVER=" + server + ";DATABASE=" + database)
uri=("xxx+pyodbc:///?odbc_connect=%s" % params)
df = dd.read_sql_table("Value", uri=uri, npartitions=10, index_col="ID", schema='', head_rows=5)

server = ''
database = ''
username = ""
password = ""

params = urllib.parse.quote_plus("DRIVER={xxxx};SERVER=" + server + ";DATABASE=" + database)
uri=("xxx+pyodbc:///?odbc_connect=%s" % params)
df = dd.read_sql_table("Value", uri=uri, npartitions=10, index_col="ID", schema='', head_rows=5)

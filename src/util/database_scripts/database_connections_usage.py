from src.util.ZW_DB_Class import TableConnection

table_connection1 = TableConnection(database='', server_name='', 
                        table_name='', schema='')

df = table_connection1.to_df()

print(table_connection1)

print(df.head())

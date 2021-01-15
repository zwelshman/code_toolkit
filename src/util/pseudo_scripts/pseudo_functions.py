import hashlib
import re

import pandas as pd

from src.util import database_connection as dbc


def append_salt(data: pd.DataFrame, column: str, salt: str) -> pd.DataFrame:
    """ Appends salt to the ID colum"""
    data[column] = data[column].astype(str) + data[column].apply(lambda x: f"{salt}")


def tokenise_dataframe(
    sourcedf: pd.DataFrame, destinationdf: pd.DataFrame, column: str
) -> pd.DataFrame:
    """ Creates a hashed columns using source and destination dataframes"""
    destinationdf["hash_" + column] = (
        pd.DataFrame(sourcedf[column].values)[0]
        .str.encode("utf-8")
        .apply(lambda x: (hashlib.sha256(x).hexdigest().upper()))
    )


def remove_salt(data: pd.DataFrame, salt: str) -> pd.DataFrame:
    """Removes the salt from the ID column"""
    data["ID"] = data["ID"].map(lambda x: str(x)[: -int(len(salt))])


def update_sql_table_hash(
    data: pd.DataFrame,
    source_table: str,
    temp_table: str,
    server: str,
    database: str,
    hash_col: str = "hash_ID",
    ID_col: str = "id",
):
    connection = dbc.connection(database=f"{database}", server=f"{server}")
    data.to_sql(
        name=f"{temp_table}",
        con=connection,
        if_exists="replace",
        schema="dbo",
        index=False,
    )
    sql = f"""UPDATE t1 SET t1.{hash_col} = t2.{hash_col} FROM {source_table} t1 INNER JOIN {temp_table} t2 ON t1.{ID_col} = t2.{ID_col};"""

    with connection.begin() as conn:
        conn.execute(sql)

import urllib
from sqlalchemy import create_engine, MetaData, Table

from typing import List, Dict
import pandas as pd


class DatabaseConnection:
    def __init__(self, database: str, server_name: str, username: str = ""):
        self._database = database
        self._server_name = server_name
        self._username = username
        self._engine = self._connect()  # type: Engine

    def _connect(self):
        param_str = f"DRIVER={{SQL Server}};SERVER={self._server_name};DATABASE={self._database};UID={self._username}"
        parse_str = urllib.parse.quote_plus(param_str)
        return create_engine(f"mssql+pyodbc:///?odbc_connect={parse_str}")


class TableConnection(DatabaseConnection):
    def __init__(
        self,
        database: str,
        server_name: str,
        username: str = "",
        table_name: str = "",
        schema: str = None,
    ):
        super().__init__(database, server_name, username)
        self._table_name = table_name
        self._schema = schema

    def connect_to_table(self):
        # Fix to current table connection issue
        metadata = MetaData()
        metadata.reflect(bind=self._engine)
        table = Table(
            f"{self._table_name}",
            metadata,
            schema=self._schema,
            autoload_with=self._engine,
        )
        return table

    def to_df(self) -> pd.DataFrame:
        df = pd.read_sql_table(self._table_name, con=self._engine, schema=self._schema)
        return df

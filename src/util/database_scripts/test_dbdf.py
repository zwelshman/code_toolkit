from src import __version__
from src.databaseConn import sqltoDF, get_connection_strings
import pandas as pd
from pandas.util.testing import assert_index_equal


def test_dbDF():
    """Tests function that reads query.sql fron src folder"""
    dfcols = sqltoDF(Query="query.sql", Path="").columns
    df2 = pd.DataFrame(
        {
            "GEOGRAPHY_CODE": [],
            "GEOGRAPHY_NAME": [],
            "OrgCode": [],
            "DH_GEOGRAPHY_NAME": [],
            "ONS_GEOGRAPHY_CODE": [],
        }
    )
    df2cols = df2.columns
    assert_index_equal(dfcols, df2cols)

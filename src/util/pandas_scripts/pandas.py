import pandas as pd

dire = '/Users/macintosh/Documents/GitHub/Toolkit/Scripts/Diabetes-Data/'

def data_prep(file) -> list:
    df = pd.read_csv(dire + file, sep='\t', header=None)
    df.columns = ['date','Hour','time','reading']
    df['date'] = pd.to_datetime(df['date'])                
    return df

def fn(df):   
    try:
        summary_stats = df.describe()
        return summary_stats
              
    except:
        raise ValueError('Check that the columns are defined properly')


df = data_prep('data-01')

fn(df)

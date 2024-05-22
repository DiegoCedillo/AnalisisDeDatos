import pandas as pd


def transform_query(query, conn):
    return pd.read_sql(query, con=conn)

def columname(df, old, new):
    return df.rename(columns={f"{old}":f"{new}"})
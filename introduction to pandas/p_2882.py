import pandas as pd


def dropDuplicateEmails(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset='email', keep='first')
    return df

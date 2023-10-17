import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students[students['student_id'] == 101]

    # Select the "Name" and "Age" columns
    df = df[["name", "age"]]
    return df

import pandas as pd
import os

def read_data_file(file_path: str)-> pd.DataFrame:
    """
    It reads the CSV file and returns Pandas DataFrame while handling path or read errors
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")

        return None
    
    try:
        df = pd.read_excel(file_path)
        print("Data loaded successfully")

        return df
    except Exception as e:
        print(f"Error reading file: {e}")

        return None


def drop_unnecessary_features(df: pd.DataFrame, cols_to_drop: list) -> pd.DataFrame:

    """
    The columns specified in cols_to_drop are dropped flexibly without relying on
    fixed names within the function

    """
    if df is None:
        return None
    
    valid_cols = [c for c in cols_to_drop if c in df.columns]

    return df.drop(columns=valid_cols)


def check_data_type(df: pd.DataFrame) -> pd.DataFrame:

    """
    It generates a quick Data Quality report that shows the data type and number of unique values for
    each column in the form of a Transposed DataFrame

    """
    if df is None:
        return None
    summary = pd.DataFrame({
        'Datatype': df.dtypes,
        'Unique Values': df.nunique()})
    
    return summary.T
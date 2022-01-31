import pandas as pd


def load(path_in_str : str) -> pd.DataFrame:
    """
    Method to read data from .xlsx files to Pandas dataframe. Empty cell values are being replaced with zeros ('0).

    :return: dataframe
    """

    df = pd.read_excel(path_in_str)
    df.fillna(value=0, inplace=True)
    return df

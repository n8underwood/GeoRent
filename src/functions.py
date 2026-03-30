import os.path
import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
    """
    Imports data from a file and returns a Pandas DataFrame.

    Parameters
    ----------
    filename : str
        File path ending in .csv
    
    Returns
    -------
    pandas.DataFrame
    """

    try: 
        os.path.exists(filename)
    except:
        raise FileNotFoundError("Invalid file path.")

    root, extension = os.path.splitext(filename)
    df = pd.DataFrame()

    if extension == ".csv":
        df = pd.read_csv(filename)
    else:
        raise ValueError("Incorrect file type. File must be a CSV.")

    if df.empty:
        raise ValueError("Empty file. Enter a file with data.")

    return df

def main():

    dfU = import_data("data/unemployment2023.csv")
    dfCL = import_data("data/cost_of_living_us.csv")

    return 0

if __name__ == "__main__":
    main()
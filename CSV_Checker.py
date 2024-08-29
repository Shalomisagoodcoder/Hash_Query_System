import pandas as pd
from File_Name import csv_file_name

def scan_and_read_CSV_file():
    try:
        df = pd.read_csv(csv_file_name)
        return df

    except FileNotFoundError as e:
        print('#' * 140)
        print(f"FileNotFoundError: {e}.")
        print("\nHere are 2 possible reason for this error:")
        print("-The excel file is not in the same directory as your script")
        print("-You misspelled the file name in File_Name.py")
        print('#' * 140)
        return None

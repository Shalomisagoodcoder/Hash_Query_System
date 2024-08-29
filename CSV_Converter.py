import pandas as pd
import os

def xlsx_to_csv(input_file, output_file=None):
    # Check if the input file exists
    if not os.path.exists(input_file):
        return

    # Read the Excel file
    df = pd.read_excel(input_file)

    # Determine output file name if not provided
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.csv'

    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Successfully converted {input_file} to {output_file}\n")

import pandas as pd

read_file = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
read_file.to_excel (r'Path to store the Excel file\File name.xlsx', index = None, header=True)
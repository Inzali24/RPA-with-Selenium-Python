import glob
import pandas as pd
# getting excel files from Directory Desktop
import xarray as xarray

path = "D:\ExcelFileForTest"
col_list = ["Total Blanks", "Correct Answers", "Submissions"]
# read all the files with extension .xlsx i.e. excel
filenames = glob.glob(path + "\*.csv")
print('File names:',  filenames)

# for loop to iterate all excel files
for file in filenames:
    # reading excel files
    print("Reading file = ", file)
    df = pd.read_csv(file, usecols=col_list)
    df_sum = xarray.DataArray.sum(data=df)
    print(df_sum)

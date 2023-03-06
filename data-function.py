# import necessary libraries
import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files
# in the folder
# set the path (source) and destination
path = os.path.dirname('data/ASP_Drug/')
destination = r'output/ASP_Drug/'
csv_files = glob.glob(os.path.join(path, "*.xls"))
  
# loop over the list of csv files
for f in csv_files:  
    # read the csv file
    df = pd.read_excel(f)

    # print the elements of the file
    file = f.split("\\")[-1]
    # the filename
    fileName = file.split('/')[2].split('.')[0]
    # the month on the file
    month = file.split('.')[0].split('_')[-3].split('/')[-1].split()[0]
    # the year on the file
    year = file.split('.')[0].split('_')[-3].split('/')[-1].split()[-1]
    # the name of the fee schedule
    feeScheduleType = file.split('.')[0].split('_')[-2] + ' ' + file.split('.')[0].split('_')[-1]

    # check the month and set the field to yyyy-mm-dd 
    if month == "JAN":
        convertMonth = year + "-01-01"
    elif month == "APR":
        convertMonth = year + "-04-01"
    elif month == "JUL":
        convertMonth = year + "-07-01"
    elif month == "OCT":
        convertMonth = year + "-10-01"

    # adding in a new column called Effective Date
    df['Effective Date'] = convertMonth

    # save files with .csv file format
    df.to_csv(destination + fileName, index=None, header=True)
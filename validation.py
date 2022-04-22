import pandas as pd
import numpy as np

df = pd.read_csv('crash_data.csv')


def crashDate(df):
    #First find all crashes
    vehicle = df["Total Vehicle Count"].dropna()

    #Format to int
    vehicle = vehicle.apply(np.int64)

    #Check to see if every crash involved a vehicle
    assert vehicle.all() >= 0, 'Only Crashes invloving vehicles allowes'
    print("True")

def crashMonth(df): #Every crash occured in August
    month = df["Crash Month"].dropna()

    month = month.apply(np.int64)

    if(month.all == 8):
        print("Crashes Occured in August")
    else:
        print("False")

def uniqueID(df):
    id = df["Serial #"].dropna()
    print(id)

    #Print duplicate rows
    dupl = id[id.duplicated()]

    if(dupl.any()):
        print("Duplicate Rows")
    else:
        print("All unique")

#crashDate(df)
#crashMonth(df)
uniqueID(df)




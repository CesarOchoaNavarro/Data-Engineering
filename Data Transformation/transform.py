from asyncio.windows_events import NULL
import pandas as pd
import numpy as np
import re

#df = pd.read_csv('books.csv')

def dropC():
    #Drop Method
    df = pd.read_csv('books.csv')
    df2 = df.drop(columns=['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks'])
    #print(df2)

    #Read CSV Method
    cols = df.columns
    dlt = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks']
    dataf = pd.read_csv('books.csv', usecols=[i for i in cols if i not in dlt])
    #print(dataf)

    

def tidy():
    df = pd.read_csv('books.csv')
    df.drop(columns=['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks'], inplace=True)

    #Remove extra dates
    for index in df.index:
        #Convert to string
        txt = str(df.loc[index, 'Date of Publication'])
        #Check if empty
        if txt == 'nan':
            df.loc[index, 'Date of Publication'] = np.NAN
        else:
            temp = re.sub("[^\d]", "", txt)
            if len(temp) > 4:
                #Get exacts length ans subtract by 4
                l = len(temp) - 4
                temp = temp[:-l]

            df.loc[index, 'Date of Publication'] = temp

    #Convert to numeric
    df['Date of Publication'] = pd.to_numeric(df['Date of Publication']) 
    print(df)

def applyM():
    df = open('uniplaces.txt', 'r')
    lines = df.readlines()
    df.close()

    for index, line in enumerate(lines):
        lines[index] = line.strip()

    df_res = pd.DataFrame(columns=('City', 'Uni', 'Num'))
    i=0
    f1 = ""
    s2 = ""
    t3 = ""
    for line in lines:
        #convert to string
        if ' (' in line:
            f1 = line.split(' (')
            print(f1)

        if ' )' in line:
            s2 = line.split(')')
            print(s2) 
        
        if '[' in line:
            t3 = line.split('[')
            print(t3)

        #df_res.loc[i] = [f1[0], s2[1]]
        #i += 1
    
    print(df)

#def form():


#print(df.columns)
#dropC()
#tidy()
applyM()

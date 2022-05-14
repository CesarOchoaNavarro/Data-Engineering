from os import stat
from numpy import cov
import pandas as pd

def census():
    df = pd.read_csv('acs2017_census_tract_data.csv', usecols=['County','State', 'Income','TotalPop','Poverty','IncomePerCap'])
    state = df.loc[df["State"] == "Texas"]
    percent = state.loc[df["County"] == "Loving County"]
    print(percent) 

    #% Poverty
    count = percent["Poverty"].div(100)
    total_perc = (count.sum() / count.count()) * 100
    print("% Poverty", total_perc)

    #Total Population
    #county_info = df.groupby(['State','County']).sum()
    total_pop = percent.groupby(['State','County']).sum()
    print(total_pop["TotalPop"])

    #PerCapitalIncome
    perCapInc = percent["Income"].sum() / total_pop["TotalPop"].iloc[0]

    print("Per Cap Income: ", perCapInc * 100000)

    county_info = df.groupby(['State','County']).sum()
    max_cal = county_info["TotalPop"].min()
    print(max_cal)

def covid():
    df = pd.read_csv('COVID_county_data.csv')
    df["date"] = pd.to_datetime(df["date"])

    #counties = df.groupby(["state", "county"]).sum()
    #print(counties)

    covid_month = df[df["date"].dt.month == 1]
    #print(covid_month)
    covid_month = covid_month[covid_month["date"].dt.year == 2021]
    #print(covid_month)

    state = covid_month.loc[df["state"] == "Oregon"]
    print(state)
    county = state.loc[df["county"] == "Malheur"]
    print(county)

    cases = county["cases"].sum()
    deaths = county["deaths"].sum()
    print(cases, deaths)



    #print(df)


#census()
covid()
import pandas as pd
import numpy as np
import matplotlib.pyplot as ply


data = pd.read_csv("C:\\data file\\covid data\\transformed_data.csv")
data2 = pd.read_csv("C:\\data file\\covid data\\raw_data.csv")
data["COUNTRY"].value_counts().mode()
# Aggregating the data

code = data["CODE"].unique().tolist()
country = data["COUNTRY"].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data2.loc[data2["location"] == i, "total_cases"]).sum())
    td.append((data2.loc[data2["location"] == i, "total_deaths"]).sum())
    sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data2.loc[data2["location"] == i, "population"]).sum()/294)

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)),
                               columns = ["Country Code", "Country", "HDI",
                                          "Total Cases", "Total Deaths",
                                          "Stringency Index", "Population"])
# Sorting Data According to Total cases
data = aggregated_data.sort_values(by=["Total Cases"], ascending= False)

# Adding to More colume (GDP per Capita before Covid-19 and GDP per Capita During covid-196)

data["GDP Before Covid"] = {65279.53, 8897.49, 2100.75,
                            11497.65, 7027.61, 9946.03,
                            29564.74, 6001.40, 6424.98, 42354.41}
data["GDP During Covid"] = {63543.58, 6796.84, 1900.71,
                            10126.72, 6126.87, 8346.70,
                            27057.16, 5090.72, 5332.77, 40284.64}
data = data.head(10)
print(data)
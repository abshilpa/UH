# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:56:37 2023

@author: User
"""
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

df_countries = pd.read_csv("countries_top10.csv")
df_countries["gdp/pop"] = df_countries["GDP"] / df_countries['Population']
df_countries["pop/km2"] = df_countries["Population"] / df_countries['Area']
df_countries.to_excel("countries_top10.xlsx")
print(df_countries)

df_gdp = pd.read_csv("GDP_2015dollars.CSV")
print(df_gdp.head())

plt.figure(1)
for country in ("China", "Germany", "Japan", "United States"):
    plt.plot(df_gdp['Year'], df_gdp[country], label=country)
    
plt.legend()
plt.xlabel("Year")
plt.ylabel("GDP(2015 $)")
plt.yscale("log")    
plt.show()
for country in ("China", 'Germany', "Japan"):
    df_gdp[country + "rel"] = 100 * df_gdp[country] / df_gdp["United States"]
    
plt.figure(2)
for country in ("china", "Germany", "Japan"):
    plt.plot(df_gdp["Year"], df_gdp[country + "rel"], label = country)
    
plt.legend()
plt.xlabel("Year")
plt.ylabel("GDP relative to USA (%)")
plt.yscale("log")    
plt.show()

df_gdp.set_index("Year", inplace=TRUE)
print(df_gdp.loc[2011:2020])

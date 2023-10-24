# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:33:54 2023

@author: User
"""


import matplotlib.pyplot as plt

# Market capitalizations
companies = ['Barclays', 'BP', 'Tesco', 'Vodafone']
market_caps = [33367, 68785, 20979, 29741]  # in millions of pounds

# Total market cap of the FTSE100
total_market_cap_ftse100 = 1814000  # in millions of pounds

# Calculate the percentage of market cap for each company
percentages = [(cap / total_market_cap_ftse100) * 100 for cap in market_caps]

# (a) Pie Chart for the Four Companies
plt.figure(figsize=(8, 8))
plt.pie(market_caps, labels=companies, autopct='%1.1f%%', startangle=140)
plt.title('Market Capitalization of Four Companies')
plt.axis('equal')
plt.show()

# (b) Pie Chart Showing Market Capitalization as a Fraction of the FTSE100
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=companies, autopct='%1.1f%%', startangle=140)
plt.title('Market Capitalization as a Fraction of FTSE100')
plt.axis('equal')
plt.show()

# (c) Bar Plot of Market Capitalizations
plt.figure(figsize=(10, 6))
plt.bar(companies, market_caps, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Company')
plt.ylabel('Market Capitalization (Million £)')
plt.title('Market Capitalization of Four Companies')
plt.show()
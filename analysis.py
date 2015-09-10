import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


als = pd.read_csv('data/analytics.csv')
df = pd.DataFrame(data=als)
Rent = df[df['Vertical'].isin(['Rent'])]
RentGroupedYear = Rent.groupby(['Year']).sum()
dff = df[df['Year'].isin([2014,2015])].groupby(['Year']).sum()
grouped = df.groupby(['Year','Vertical']).sum()

# print ".isin(['Rent','VRP'])"
print RentGroupedYear
# print df.describe()
# print als.head()
# print als
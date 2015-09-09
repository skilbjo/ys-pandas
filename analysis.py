import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


als = pd.read_csv('data/analytics.csv')
df = pd.DataFrame(data=als)

print df.groupby(['Year','Vertical']).sum()
# print df.describe()
# print als.head()
# print als
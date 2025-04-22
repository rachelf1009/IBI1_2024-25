import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/xuqiufan/Desktop/IBI")
os.getcwd()
os.listdir()
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.head(3)


print(dalys_data.iloc[0:10,2])


years=[]
for i in dalys_data.loc[:,'Year']:
    if i == 1990:
        years.append(True)
    else:
        years.append(False)
print(dalys_data.loc[years,"DALYs"])


a=dalys_data.loc[dalys_data.Entity=='United Kingdom','DALYs'].describe()['mean']
b=dalys_data.loc[dalys_data.Entity=='France','DALYs'].describe()['mean']
print(a)
print(b)
if a > b:
    print('the mean DALYs in the UK was greater than France')
if a< b:
    print('the mean DALYs in the UK was smaller than France')


uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.show()

cn = dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
merged=pd.merge(cn, uk, on="Year", suffixes=('_cn', '_uk'))
plt.plot(merged["Year"], merged["DALYs_cn"] - merged["DALYs_uk"], 'b+')
plt.xticks(merged["Year"], rotation=-90)
plt.show()
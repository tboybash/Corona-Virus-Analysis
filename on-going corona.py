

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:24:55 2020

@author: bashi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:08:49 2020

@author: bashi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 05:38:27 2020

@author: bashi
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
recoveries_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
confirmed_df['status']=['confirmed' for x in range(255)]
deaths_df['status']=['dead' for x in range(255)]
recoveries_df['status']=['recovered' for x in range(255)]


cases=confirmed_df['3/8/20']
recovered=recoveries_df['3/8/20']
dead=deaths_df['3/8/20']

confirmed_df['recovery_rate']=recovered/cases
confirmed_df['death_rate']=dead/cases



conf1 = pd.pivot_table(confirmed_df, values='3/8/20', index=['Country/Region'], aggfunc=np.sum)
recov1=pd.pivot_table(recoveries_df, values='3/8/20', index=['Country/Region'], aggfunc=np.sum)
dead1=pd.pivot_table(deaths_df, values='3/8/20', index=['Country/Region'], aggfunc=np.sum)
merg=pd.merge()

	
# Merge two Dataframes on index of both the dataframesrecov1['3/8/20']
mergedDf = conf1.merge(recov1['3/8/20'], left_index=True, right_index=True)
mergedDf = mergedDf.merge(dead1['3/8/20'], left_index=True, right_index=True)
cases=mergedDf['3/8/20_x']
recovered=mergedDf['3/8/20_y']
dead=mergedDf['3/8/20']
mergedDf['recovery_rate']=recovered/cases
mergedDf['death_rate']=dead/cases
mergedDf['cases']=cases


tab=mergedDf['cases'].sort_values(ascending=False).head(10)
ind=tab.index
tab.plot(kind='bar')
plt.ylabel("Counts of Confirmed Cases")
plt.title("Confirmed Cases of Worst Hit Countries")

tab2=mergedDf['recovery_rate'].sort_values(ascending=False).head(10)
tab2.plot(kind='bar')
tab22=mergedDf['recovery_rate'].loc[ind].sort_values(ascending=False)
tab22.plot(kind='bar')
plt.ylabel("Recovery rates")
plt.title("Recovery Rates of Worst Hit Countries")


tab3=mergedDf['death_rate'].sort_values(ascending=False).head(10)
tab3.plot(kind='bar')
tab33=mergedDf['death_rate'].loc[ind].sort_values(ascending=False)
tab33.plot(kind='bar')
plt.ylabel("Death rates")
plt.title("Death Rates of Worst Hit Countries")






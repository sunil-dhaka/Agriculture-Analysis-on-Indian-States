'''
script to get Indian states area in sq. KM from wiki html page 
'''

import pandas as pd

# specific link is from wiki
df=pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area')[1]
# extract useful info
df2=pd.DataFrame({'NAME_1':df['State (S) / Union territory (UT)'][:-1],'Area':df['Area (km2)'][:-1]})

# manual edit on area and state-names

# name change
df2.iloc[32,0]='Dadra and Nagar Haveli'
# LD and JK into JK
df2.iloc[21,1]=101387

# save into a csv
df2.to_csv('datasets/area.csv',index=False)
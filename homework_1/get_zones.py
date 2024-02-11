#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import wget
from urllib.error import HTTPError


# In[2]:

url = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
try:
  wget.download(url, out = 'taxi_zone_lookup.csv')
except HTTPError:
  print('error')

df_zones = pd.read_csv('taxi_zone_lookup.csv')


# In[3]:


df_zones.head()


# In[7]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()
df_zones.to_sql(name='green_zones', con=engine, if_exists='replace')


# In[ ]:




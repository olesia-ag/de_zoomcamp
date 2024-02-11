
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import wget

# In[2]:

url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz'
wget.download(url, out = 'green_tripdata_2019-09.csv')

df_zones = pd.read_csv('green_tripdata_2019-09.csv', compression='gzip')


# In[3]:


df_zones.head()


# In[7]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()
df_zones.to_sql(name='green_taxi_data', con=engine, if_exists='replace')


# In[ ]:




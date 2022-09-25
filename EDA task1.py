#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df=pd.read_csv(r'C:\Visadataset.csv',sep=',')


# In[8]:


df.head()


# In[9]:


df.info()


# In[10]:


df.describe()


# In[12]:


get_ipython().system('pip install dtale')


# In[16]:


import dtale
dtale.show(df,ignore_duplicate=True)


# In[22]:


get_ipython().system('pip install pandas_profiling')


# In[23]:


from pandas_profiling import ProfileReport
profile = ProfileReport(df, explorative=True)
profile


# In[24]:


get_ipython().system('pip install sweetviz')


# In[30]:


import sweetviz as sv
profile=sv.analyze(df)
profile.show_html('sweet_report.html')


# In[33]:


get_ipython().system('pip install autoviz')


# In[38]:


from autoviz.AutoViz_Class import AutoViz_Class
df_av = AutoViz_Class().AutoViz('Visadataset.csv')


# In[ ]:





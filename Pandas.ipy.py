#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Pandas
1.Pandas data


# In[1]:


get_ipython().system('pip.install pandas')


# In[3]:


import pandas as pd
import numpy as np


# In[15]:


# create a Dataframe
pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"],columns=["Column1","Column2","Column3","Column4"])


# In[13]:


df.pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"],columns=["Column1","Column2","Column3","Column4"])


# In[17]:


type(df)


# In[ ]:


df,tail(3)


# In[ ]:


df.describe()


# In[ ]:


df.head()


# In[8]:


df[['Column1','Column2','Column3','Column4']]


# In[10]:


type(df[['column1']])


# In[ ]:


pd.read


# In[20]:


pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4"],columns=["Column1","Column2","Column3","Column4"])


# In[19]:


type(data)


# In[ ]:


pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4"],columns=["Column1","Column2","Column3","Column4"])


#!/usr/bin/env python
# coding: utf-8

# Part 1: Exploratory Data Analysis (EDA)
# 

# In[ ]:





# Import libraries
# 

# In[2]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv('hotel_booking.csv')


# In[4]:


df.head(10)


# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.describe()


# In[10]:


df.isna().sum()


# In[ ]:





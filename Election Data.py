#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
survey = pd.read_excel('Sample Survey.xlsx')
print (survey)


# In[2]:


survey['count'] = 1
survey.groupby(['collection_date']).count()['count']


# In[3]:


x = sum(survey['age'].value_counts().loc[lambda x : x>45])
y = sum(survey['age'].value_counts())
x/y*100


# In[4]:


age_group = survey.assign(agegroup=pd.cut(survey['age'], bins=[0,18,25,40,55], right=False, labels=['18-25','25-40','40-55','55+']))
cols = list(age_group.columns)
age_group = age_group[[cols[0]]+[cols[-1]]+[cols[9]]]
age_group


# In[5]:


age_group['agegroup'].value_counts()


# In[6]:


age_group['agegroup'].value_counts()[:1].sort_values(ascending=False)


# In[7]:


proportion_1 = survey['Vote_Now'].value_counts(normalize=True) * 100
proportion_1.loc[["RJD"]]
proportion_2 = survey['Past_Vote'].value_counts(normalize=True) * 100
proportion_2.loc[["RJD"]]
proportion_1.loc[["RJD"]],proportion_2.loc[["RJD"]]


# In[10]:


survey['count'] = 1
(survey.groupby(['collection_date','MLA_satisfaction']).count()['count'])/(survey.groupby(['collection_date']).count()['count'])*100


# In[11]:


survey['count'] = 1
(survey.groupby(['collection_date','CM_satisfaction']).count()['count'])/(survey.groupby(['collection_date']).count()['count'])*100


# In[ ]:





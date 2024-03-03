#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[15]:


data= pd.read_csv("C:\\Users\Layefa\Dropbox\PC\Downloads\dataset_instagram-post-scraper_2024-03-03_18-41-39-456.csv")


# In[16]:


data.head()


# In[17]:


data.info()


# In[18]:


data.describe()


# In[19]:


data.isnull().sum()


# In[27]:


data.duplicated()


# In[30]:


df= pd.DataFrame(data)


# In[31]:


#separating the date from time in the timestamp column

df['timestamp'] = pd.to_datetime(df['timestamp'])


# In[36]:


df['date'] = df['timestamp'].dt.date
df['time'] =df['timestamp'].dt.time

print(df)


# In[66]:


# dropped row 2 and 10. aslo row 0, 4, 7 because they are older date data. 2022 and 2023. 
#We are working with the February 2024 data

df= df.drop([0, 4, 7])
print(df)


# In[67]:


#replacing the NAN values with 'photo' because those are photo posts 

df= df.fillna('photo')
print(df)


# In[59]:


#arranging the date in an ascending order 

df= df.sort_values(by='date')
print(df)


# In[114]:


df


# In[104]:


#plotting the amount of likes in the days in february

plt.figure(figsize=(15, 10))
sns.set_theme(style= "whitegrid")
plt.title('Total Likes in February by Date')
sns.barplot(x= 'likesCount', y='date', data=df)
plt.show()


# In[84]:


# Correlation matrix to identify relationships between variables
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Heatmap for correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Between Likes and Comments')
plt.show()


# In[82]:


# Countplot for categorical variables

plt.figure(figsize=(8, 6))
sns.countplot(x='commentsCount', data=df)
plt.title('Number of comments by posts')
plt.show()


# In[83]:


# Countplot for categorical variables

plt.figure(figsize=(8, 6))
sns.countplot(x='likesCount', data=data)
plt.title('Count of likes by Number of Posts')
plt.show()


# In[105]:


plt.figure(figsize=(15, 10))
sns.set_theme(style= "whitegrid")
plt.title('Total Comments in February by Time')
sns.barplot(x= 'commentsCount', y='time', data=df)
plt.show()


# In[106]:


plt.figure(figsize=(15, 10))
sns.set_theme(style= "whitegrid")
plt.title('Total Likes in February by Time')
sns.barplot(x= 'likesCount', y='time', data=df)
plt.show()


# In[107]:


plt.figure(figsize=(15, 10))
sns.set_theme(style= "whitegrid")
plt.title('Total Comments in February by Date')
sns.barplot(x= 'commentsCount', y='date', data=df)
plt.show()


# In[119]:


#showing full caption of the highest comments and highest likes

df_selected = df.loc[[8, 18], ['caption', 'date', 'time']]
pd.set_option('display.max_colwidth', -1)  
df_selected.rename(index={8: 'Comments', 18: 'Likes'}, inplace=True)
df_selected = pd.DataFrame(df_selected)
df_selected


# In[ ]:





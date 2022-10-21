#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr_np=np.random.randint(1,20,(15))
print(arr_np)
#Using NumPy creating random vector of size 15 having only Integers in the range 1-20


# In[5]:


arr_np=np.reshape(arr_np,(3,5))#reshaping array
print(arr_np)


# In[6]:


for i in arr_np:
    i[np.where(i==i.max())]=0
print(arr_np)
#Replacing the max in each row by 0


# In[ ]:


In [5]:
  


# In[1]:


import pandas as p
df = p.read_csv('//Users//jagadeeshreddy//Desktop//data.csv')
print(df.head(20))
column_means = df. mean()#returns the mean values
print(column_means)


# In[2]:


df = df. fillna(column_means)#to replace null values with mean
print(df.head(20))#returns number of rows


# In[3]:


result = df.groupby(['Pulse','Duration']).agg({'Maxpulse': ['mean', 'min','max', 'count'],'Pulse': ['mean', 'min', 'max', 'count']})
print(result)
#Selecting a two columns and aggregate the data using: min, max, count, mean.


# In[7]:


filtered_df1=df[(df['Calories'] > 500) & (df['Calories'] < 1000)]
filtered_df2=df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(filtered_df2)
#Filtering the dataframe to select the rows with calories values between 500 and 1000.
#Filtering the dataframe to select the rows with calories values > 500 and pulse < 100. 


# In[8]:


df_modified = df.loc[:, df.columns != 'Maxpulse']
print(df_modified)
#Creating a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.


# In[10]:


df.drop('Maxpulse', inplace=True, axis=1)#delete maxpulse 1 for columns
print(df.dtypes)

df.plot.scatter(x='Duration',y='Calories')#creating a scatter plot
df


# In[11]:


import matplotlib.pyplot as plt
import numpy as np
 
main_arr = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
labels_data = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myexplode_data = [0.2, 0, 0, 0,0,0]
plt.pie(main_arr,labels=labels_data, explode = myexplode_data,autopct='%1.1f%%')
plt.show()


# In[ ]:





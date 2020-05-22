#!/usr/bin/env python
# coding: utf-8

# In[10]:


#QUESTION-1
"""Create a data frame which holds the three columns m x and c store numerical data in each column. 
Add a new column called y. The content of y is the output obtain when we make use of equation of y=mx+c. 
Plot the graph to obtain a straight line using the data frame contents."""

import pandas as pd 
 # initialize list of lists 
data = [[10,2,5], [5,8,3], [6,7,2]] 
 
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['m', 'x','c']) 
 
# print dataframe. 
df


df['y'] = df.apply(lambda row: (row.m*row.x)+row.c, axis=1)
print(df)


print("ploting the graph")
import matplotlib.pyplot as plt
df.plot(kind='line',x='x',y='y',color='red')
plt.show()


# In[11]:


#2.Create series called result which is the column y
result=pd.Series(df['y'])
print(result)


# In[26]:


#3.Using a csv file create a data frame for any time series data and perform some mathematical operations on it
data=pd.read_csv("C:/Users/christ/Downloads/gdp.csv")
print(type(data))
#using count function
print("count")
print(data.count()) 
  
#using sum function 
print("sum")
print(data.sum()) 
  
#using mean function 
print("mean")
print(data.mean())  
  
#using std function
print("std")
print(data.std()) 
  
#using min function 
print("minimum")
print(data.min()) 
  
#using max function
print("maximum")
print(data.max()) 
  
#using median function 
print("median")
print(data.median()) 
  


# In[ ]:


#Explore various functions available in pandas with respect to data frames and data series.



# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from pandas import Series,DataFrame


# ## 线形图 df.plot()    
# ### 直线、折线

# In[2]:


plt.plot(np.arange(20))
plt.show()


# In[3]:


plt.plot(np.array([2.5, 4.1, 2.7, 8.8, 1.0]))
plt.show()


# In[4]:


series=Series(np.array([2.5, 4.1, 2.7, 8.8, 1.0]))
series.plot()
plt.show()


# In[5]:


# 注意x轴索引，是伸缩的，不是典型坐标系
dataframe=DataFrame({'A':[9.3, 4.3, 4.1, 5.0, 7.0], 'B':[2.5, 4.1, 2.7, 8.8, 1.0]})
dataframe.plot()
plt.show()


# In[6]:


# dashed属性表示虚线
series.plot(linestyle='dashed', color='k', marker='o')
plt.show()


# In[7]:


# xtick,ytick表示x轴和y轴的刻度，xlim表示限制范围
dataframe.plot(title='dataframe photo',linestyle='dashed', color='k', marker='o',
               xticks=[0, 1, 2, 3, 4], yticks=list(np.arange(0, 10.0, 0.5)) ,
               xlim=[1, 3])
dataframe.plot(title='dataframe photo')
plt.show()


# In[8]:


# 在绘图命令中加入subplots=True参数，则会将DataFrame当中的每一列结果绘制到一个子图片中，如果加入sharex=True参数，则各个子图片共用一个X轴标签；同理sharey=True表示共用一个Y轴
dataframe.plot(subplots=True, sharex=True) 
plt.show()


# ## 柱状图 df.plot(kind='bar')
# ### 显示值的大小

# In[9]:


# Series和DataFrame的索引将会被用作X（bar）或Y（barh）刻度 
dataframe.index=['once', 'twice', 'thrice', 'forth', 'fifth']
dataframe.plot(kind='bar')
dataframe.plot(kind='barh') 
# x轴黑线标识
plt.axhline(0, color='k')
plt.show()


# In[10]:


dataframe['A'].plot(kind='bar')
plt.show()


# In[11]:


df=DataFrame({'part A': [2.8, 5.5, 5.5, 2.8, 2.8], 'part B': [4.2, 1.2, 4.5, 2.5, 
    8.0], 'part C': [3.3, 3.3, 1.0, 1.0, 1.0]}, index=['May', 'June', 'July', 
                                                    'August', 'September']) 
df.name='bonus'
df


# In[12]:


df.plot(kind='bar')
df.plot(kind='bar', stacked=True)
plt.show()


# In[13]:


# 离散型变量个数分布图
df['part C'].value_counts().plot(kind='bar')
plt.show()


# In[14]:


#两个离散型变量的关系图
temp1=df['part A'][df['part C']==3.3].value_counts()
temp2=df['part A'][df['part C']==1.0].value_counts()
temp=DataFrame({'0':temp1,'1':temp2})
temp.plot(kind='bar',stacked=True)
plt.show()


# In[15]:


# 连续性变量和离散型变量的关系图
plt.scatter(df['part C'],df['part B'])
plt.show()


# ## 直方图 df.plot.hist()
# ### 对连续值离散化，划分一个个小区间，然后统计每个区间的数目

# In[16]:


length=DataFrame({'length': [10, 20,15,10,1,12,12,12,13,13,13,14,14,14,51,51,51,51,
                             51,4,4,4,4]}) 
length.plot.hist()
plt.show()


# ### 利用获得的直方图可以绘制密度图，绘制的图形是根据直方图得到的条状分布的顶点连接后得到的平滑曲线
# 

# In[17]:


length=DataFrame({'length': [10, 20,15,10,1,12,12,12,13,13,13,14,14,14,51,51,51,51,
                             51,4,4,4,4]}) 
# 两者等价
length.plot.kde(color='k')
length.plot.density(color='k')
plt.show()


# In[18]:


df4 = DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c': np.random.randn(1000) - 1}, index=range(1,1001), columns=['a', 'b', 'c'])
df4.a.plot.hist(stacked=True)
plt.show()


# In[19]:


# 将a的值进行累加
df4['a'].plot.hist(cumulative=True)
plt.show()


# In[20]:


# 每列单独画图
df4.diff().hist()
plt.show()


# ## 箱线图 df.plot.box()

# In[21]:


df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()
plt.show()


# In[22]:


color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray') 
df.plot.box(color=color)
plt.show()


# In[23]:


df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B']) 
# df.plot.box(by='X') 得不到分组结果
df.boxplot(by='X')
plt.show()


# In[24]:


df = pd.DataFrame(np.random.rand(10,3), columns=['Col1', 'Col2', 'Col3']) 
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B']) 
df['Y'] = pd.Series(['A','B','A','B','A','B','A','B','A','B']) 
df 


# In[25]:


plt.figure()
bp = df.boxplot(column=['Col1','Col2'], by=['X','Y'])
plt.show()


# ## 区域面积图df.plot.area()

# In[26]:


df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd']) 
df


# In[27]:


df.plot.area() #生成堆积图 
# df.plot.area(stacked=False) #非堆积效果图
plt.show()


# ## 散点图 plot.scatter()

# In[28]:


df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df


# In[29]:


df.plot.scatter(x='a', y='b')
plt.show()


# In[30]:


ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1')
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax) 
plt.show()


# ## 饼图 df.plot.pie()

# In[31]:


series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
series


# In[32]:


series.plot.pie(figsize=(6, 6))
plt.show()


# In[33]:


df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y']) 
df


# In[34]:


df.plot.pie(subplots=True, figsize=(8, 4))
plt.show()


# In[35]:


series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series') 
series 


# In[36]:


series.plot.pie(colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6))
plt.show()


# In[37]:


series = pd.Series([0.1] * 4, index=['a', 'b', 'c', 'd'], name='series2') 
series 


# In[38]:


series.plot.pie(figsize=(6, 6)) 
plt.show()


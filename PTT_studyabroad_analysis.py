#!/usr/bin/env python
# coding: utf-8

# # Import packages and read data

# In[1]:


import pandas as pd
df=pd.read_csv('studyabroad_ptt.csv')


# In[2]:


from matplotlib import pyplot as plt
import plotly.graph_objects as go
from wordcloud import WordCloud 
import numpy as np
import matplotlib.pyplot as plt
import jieba
import jieba.analyse


# # Data cleaning
# 

# In[3]:


#date formating
from datetime import datetime
df.date=df.date.replace('Sat Feb 15 15:18','Sat Feb 15 15:18:00 2020')
df['date']=df['date'].apply(lambda x : None if x=='no date' else(datetime.strptime(x,"%a %b %d %H:%M:%S %Y")))


# In[4]:


#check for null values
df.isnull().sum()


# In[5]:


df.push=df.push.fillna(0)
df=df.dropna(subset=['date'])
df=df.drop(columns=['Unnamed: 0'])
df=df.drop_duplicates()


# In[6]:


df.info()


# In[7]:


df[df.date==datetime.strptime('2020-01-05 10:38:40',"%Y-%m-%d %H:%M:%S")]
df=df.drop(21)


# In[8]:


df.columns = ['headline','date','author',
              'push','boos','pushina',
              'neutral','content','comment',
              'weblink','numofcomments']


# # Visualization

# In[9]:


df=df.sort_values(by='date')
#filter data from 2020/1/1 to 2020-08-17
start_date='2020-01-01 00:00:00'
end_date='2020-08-17 23:59:59'
after_startdate=df['date']>=datetime.strptime(start_date,"%Y-%m-%d %H:%M:%S")
before_enddate=df['date']<=datetime.strptime(end_date,"%Y-%m-%d %H:%M:%S")
between_two_dates = after_startdate & before_enddate
filtered_dates=df.loc[between_two_dates]


# In[10]:


filtered_dates.shape


# In[11]:


fig = go.Figure([go.Scatter(x=filtered_dates['date'], y=filtered_dates['numofcomments'])])
fig.show()


# In[12]:


virus_name=[]
with open('virus name.txt','r',encoding='UTF-8') as file:
    for data in file.readlines():
        data=data.strip()
        virus_name.append(data)

filtered_dates=filtered_dates.reset_index()


#count the number of comments mentioned virus
numofc=[]  
for i in range(0,1077):
    segment=filtered_dates.comment[i]
    if (isinstance(segment,list)==True):
        counts=0
        for j in segment:
            words=jieba.lcut(j)
            count=0
            for w in words:
                if w in virus_name:
                    count=count+1
            counts=counts+count
        numofc.append(counts)
    else:
        segment=segment.split(', ')
        counts=0
        for j in segment:
            words=jieba.lcut(j)
            count=0
            for w in words:
                if w in virus_name:
                    count=1
            counts=counts+count
        numofc.append(counts) 


# In[13]:


df=pd.Series((i for i in numofc)) 
df=pd.DataFrame(df, columns=['numofcomments_e'])
filtered_dates=pd.concat([filtered_dates,df],axis=1)


# In[14]:


fig = go.Figure([go.Scatter(x=filtered_dates['date'], y=filtered_dates['numofcomments_e'])])
fig.show()


# In[15]:


filtered_dates.head()


# In[16]:


line1 = go.Scatter(x=filtered_dates['date'], y=filtered_dates['numofcomments'])
line2 = go.Scatter(x=filtered_dates['date'], y=filtered_dates['numofcomments_e'])
data = [line1, line2]
layout = go.Layout(title='Comments vs comments discussed virus',
                    yaxis=dict(title='commnets and comments discussed virus'))
go.Figure(data=data,layout=layout)


# In[17]:


x=filtered_dates[['date','headline','numofcomments_e','numofcomments']].sort_values(ascending=False,by="numofcomments_e")[0:10]
x.sort_values(ascending=False,by="numofcomments")[0:3]


# In[18]:


filtered_dates[(filtered_dates['numofcomments_e']>0)]['numofcomments_e'].mean()


# In[19]:


filtered_dates['numofcomments'].mean()


# In[20]:


before=filtered_dates[(filtered_dates['numofcomments']>filtered_dates['numofcomments'].mean())&(filtered_dates['numofcomments_e']>4)&(filtered_dates['date']<datetime.strptime('2020-03-21 00:00:00',"%Y-%m-%d %H:%M:%S"))]


# In[21]:


before[['date','headline','numofcomments_e','numofcomments']].sort_values(ascending=False,by="numofcomments")


# In[22]:


comments=[]
for i in before.comment:
        comments.append(i)
allcomment=' '.join(comments)


# In[23]:


def generate_segment(x):
    x=x.replace('[','')
    x=x.replace(']','')
    x=x.replace("'", '')
    x=x.replace(".", '')
    x=x.split(', ')
    listofsentence=[]
    for j in range(0,len(x)):
        seg_list=jieba.lcut(x[j])
        segmentlist=' '.join(seg_list)
        listofsentence.append(segmentlist)
    allsegmentlist=' '.join(listofsentence)
    return(allsegmentlist)



stopwords=[]
with open('stopwords.txt','r',encoding='UTF-8') as file:
    for data in file.readlines():
        data=data.strip()
        stopwords.append(data)

def generate_wordcloud(x):
    texts=x.split(' ')
    words=[]
    for i in texts:
        if i not in stopwords:
            words.append(i)
    wordsforwc=' '.join(words)
    wc=WordCloud(font_path="NotoSerifCJKtc-Black.otf",background_color='white',max_words=200,stopwords='stopwords.txt')
    wc.generate(wordsforwc)
    
    plt.imshow(wc)
    plt.axis("off")
    plt.figure(figsize=(20,10), dpi = 100)
    plt.show()
    print(jieba.analyse.extract_tags(wordsforwc, topK=20, withWeight=False, allowPOS=()))


# In[24]:


generate_wordcloud(generate_segment(allcomment))


# In[25]:


after=filtered_dates[(filtered_dates['numofcomments']>filtered_dates['numofcomments'].mean())&(filtered_dates['numofcomments_e']>4)&(filtered_dates['date']>=datetime.strptime('2020-03-21 00:00:00',"%Y-%m-%d %H:%M:%S"))]


# In[26]:


after[['date','headline','numofcomments_e','numofcomments']].sort_values(ascending=False,by="numofcomments")


# In[27]:


comments=[]
for i in after.comment:
        comments.append(i)
        allcomment=' '.join(comments)


# In[28]:


generate_wordcloud(generate_segment(allcomment))


# In[29]:


filtered_dates[['date','headline','numofcomments_e','numofcomments']].sort_values(ascending=False,by="numofcomments")[0:10]


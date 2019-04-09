#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('working')


# In[4]:


from nltk.stem import SnowballStemmer
SnowballStemmer.languages
fs=SnowballStemmer('french')
fs.stem('manager')


# In[5]:


fs.stem('working')


# In[6]:


stemmerporter.stem('farmer')


# In[7]:


fs.stem('farmer')


# In[8]:


from nltk.stem import LancasterStemmer
sl=LancasterStemmer()
sl.stem('working')
sl.stem('happiness')


# In[9]:


sl.stem('working')


# In[10]:


stemmerporter.stem('Nidhi')


# In[11]:


stemmerporter.stem('farming')


# In[12]:


sl.stem('teacher')


# In[13]:


sl.stem('teaching')


# In[14]:


sl.stem('teaches')


# In[15]:


stemmerporter.stem('connect')


# In[16]:


stemmerporter.stem('connected')


# In[17]:


stemmerporter.stem('connecting')


# In[18]:


stemmerporter.stem('connection')


# In[20]:


stemmerporter.stem('connections')


# In[21]:


fs.stem('connect')


# In[22]:


fs.stem('connected')


# In[23]:


fs.stem('connecting')


# In[24]:


fs.stem('connection')


# In[25]:


fs.stem('connections')


# In[26]:


sl.stem('connect')


# In[27]:


sl.stem('connected')


# In[28]:


sl.stem('connecting')


# In[29]:


sl.stem('connection')


# In[30]:


sl.stem('connections')


# In[31]:


from nltk.stem import RegexpStemmer
rx=RegexpStemmer('ing')
rx.stem('working')


# In[32]:


rx.stem('working')


# In[33]:


rx.stem('farming')


# In[34]:


rx.stem('happiness')


# In[35]:


rx=RegexpStemmer('in')
rx.stem('working')


# In[ ]:





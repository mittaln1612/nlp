#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
nltk.download()


# In[ ]:


from nltk.corpus import brown
brown.categories()


# In[ ]:


brown.categories()


# In[ ]:


brown.words(categories='adventure
            ')


# In[ ]:


brown.words(categories='adventure')


# In[ ]:


brown.words(categories='adventure')[:20]


# In[ ]:


brown.characters(categories='religion')


# In[ ]:


inaugural.fileids()


# In[ ]:


from nltk.corpus import inaugural
inaugural.fileids()


# In[ ]:


inaugural.words(fileid='2009-Obama.txt')


# In[ ]:


inaugural.words(fileids='2009-Obama.txt')[:100]


# In[ ]:





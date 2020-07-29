#!/usr/bin/env python
# coding: utf-8

# #  make a new dictionary in which keys become values and values become keys

# In[1]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}


# In[2]:


port2 = dict([(value, key) for key, value in port1.items()])


# In[3]:


print ("Original dictionary is : ",port1)
print ("swap dictionary is : ",port2)


# # Make a new list which contains the sum of the number of tuples.

# In[4]:


listtupple=[(1,2), (3,4), (5,6),(4,5)]


# In[6]:


res = [(sum(lst)) for lst in listtupple]


# In[7]:


print(res)


# In[ ]:





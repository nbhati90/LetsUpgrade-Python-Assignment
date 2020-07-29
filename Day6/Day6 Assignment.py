#!/usr/bin/env python
# coding: utf-8

# # Convert to a dictionary in one line code using list comprehension (without using zip method)

# In[1]:


List1 = [1,2,3,4,5,7,8]
List2 = ["a", "b", "c", "d", "e","f","g","h"]


# In[2]:


res = {} 
for key in List1: 
    for value in List2: 
        res[key] = value 
        List2.remove(value) 
        break
print(res)


# In[ ]:





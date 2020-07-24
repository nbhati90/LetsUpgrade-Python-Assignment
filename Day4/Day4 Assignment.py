#!/usr/bin/env python
# coding: utf-8

# # Find all occurrence of substring in the given string

# In[2]:


value="what we think we become; we are Python programmer"
finding="we"
res = [i for i in range(len(value)) if value.startswith(finding, i)]
print("The start indices of the substrings are : " + str(res)) 


# # Explain using islower() isupper() with different kinds of strings.

# In[16]:


one = "welcome to the new world"
two = "welcome to The NEW World"
three = "welcome to the new world 123"
four = "welcome to the new world##$%"
print(one.islower())
print(two.islower())
print(three.islower())
print(four.islower())


# In[18]:


one = "WELCOME TO THE NEW WORLD"
two = "WELCOME TO THE new WORLD"
three = "WELCOME TO THE NEW WORLD 123"
four = "WELCOME TO THE NEW WORLD##$%"
print(one.isupper())
print(two.isupper())
print(three.isupper())
print(four.isupper())


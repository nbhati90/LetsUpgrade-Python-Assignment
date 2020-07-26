#!/usr/bin/env python
# coding: utf-8

# # Sort by increasing order but all zeros should be at the right hand side.

# In[19]:


def myFunc(e):
  return e==0

list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list1.sort()
list1.sort(key=myFunc)
print(list1)


# # Merge these two sorted lists to produce one sorted list, but use only loop either while or for only one time

# In[30]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list1.extend(list2)
print("Adding the two list : ",list1)

i=0
while i<len(list1):
    key=i
    j=i+1
    while j<len(list1):
        if list1[key]>list1[j]:
            key=j
        j+=1
    list1[i],list1[key]=list1[key],list1[i]
    i+=1
print("After the while loop: ",list1)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Back Slash

# In[13]:


print("Hello       world")


# # Tiple Quotes

# In[15]:


print ("""      
─────█─▄▀█──█▀▄─█─────
────▐▌──────────▐▌────
────█▌▀▄──▄▄──▄▀▐█────
───▐██──▀▀──▀▀──██▌───
──▄████▄──▐▌──▄████▄──     \
Welcome to python""")


# # String Inside the quotes

# In[17]:


print ("I don't know python")


# if you start with double quotes the end with double quotes

# In[18]:


print ("hello\a")


# In[28]:


name = "Nikesh"
age = 25
percentage = 90.6
print("My name is",name,"and age is",age,"and my percentage is",percentage)


# In[29]:


print("My name is %s and age is %10d and my percentage is %0.2f"%(name,age,percentage))


# Here you are using 10 for the gap and 0.2 is for float round of after 2 point.

# In[30]:


print(f"My name is {name} and age is {age} and my percentage is {percentage}")


# # Variable and how to assign

# In[3]:


a=b=c=10
print(f"A value is {a}")
print(f"B value is {b}")
print(f"C value is {c}")


# In[32]:


id(a)


# id here is locating memory address

# # Operators in Python

# # Arithmetic Operators

# In[33]:


print(5**2)
print(5*2)
print(5+2)
print(5-2)
print(5/2)
print(5%2)
print(5//2)


# # Comparision Operators

# In[2]:


x=y=10
z=20
print(x==y)
print(x==z)
print(x>z)
print(x<z)
print(x>=y)
print(x<=y)
print(x!=z)
print(x!=y)


# # assignment Operator

# In[4]:


x+=5
print(x)
y-=5
print(y)
z*=5
print(z)
a/=5
print(a)
b%=5
print(b)
c**=5
print(c)


# # BitWise Operator
p=5  0101
q=2  0010
# In[5]:


p=5
q=2

print(p|q)
print(p&q)
print(~p)
print(p^q)
print(p<<2)
print(q>>2)


# In[6]:


print(10>9 and 9<5)
print(10>9 or 9<5)
print(not 9<5)


# # Operator Precedence

# In[8]:


print(10+15/2**2%5)


# this is BODMAS Technic

# In[ ]:





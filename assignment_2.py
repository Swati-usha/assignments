#!/usr/bin/env python
# coding: utf-8

# In[55]:



for i in range(6):
    for j in range(i):
        print("*",end=' ')
    print(" ")
for k in range(4,0,-1):
    for l in range(k):
        print("*",end=' ')
    print(" ")    


# ## Write a Pyhton program to reverse a word after accepting the input from the user.

# In[57]:


user_input = input("Enter the word : ")
print(user_input[::-1])


# In[ ]:





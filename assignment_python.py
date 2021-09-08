#!/usr/bin/env python
# coding: utf-8

# ## Code which will find all such numbers which are divisible by 7 but are not a multiple of 5, btw 2000 and 3200(both included).

# In[7]:


for i in range(2000,3201):
    if i%7==0:
        if i%5 !=0:
            print(str(i) + ',',end='')


# ## Python Program to accept user's first and last name and print them in the reverse order with a space btw the first name and last name

# In[10]:


f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

print(l_name[::-1] + " " + f_name[::-1])


# ## Write a python program to find the volume of a sphere with diameter 12 cm
# 

# In[18]:


import math

diameter = 12
radius = diameter/2

radii_cube = pow(radius,3)
prod_pi = radii_cube*math.pi

volume = (4/3)*prod_pi
print("Volume Of Sphere is : " , volume)


# In[ ]:





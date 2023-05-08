#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

print("Welcome to my Dice rolling game")
while (True):
    print(random.randint(1,6))
    roll_again = input("if you wants to roll the dice again\npress y else n\n")
    if roll_again == 'y':
          continue
    else :
          break


# In[ ]:





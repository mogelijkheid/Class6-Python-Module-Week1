#!/usr/bin/env python
# coding: utf-8

# In[ ]:


length = float(input("What is your lenght?:"))
weight = float(input("What is your weight?:"))
indeks = weight/(length*length)
if indeks < 25:
    print("normal")
elif 25< indeks < 30:
    print("overweight")
elif 30< indeks < 40:
    print("obese")
elif indeks > 40:
    print("extremely obese")


# In[ ]:





# In[ ]:





# In[ ]:





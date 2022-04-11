#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name=input("Enter your name:")
surname=input("Enter your surname:")
student_number=input(" Enter your student number:")
course=list()
visa=list()
final=[]
result=[]
for i in range(4): 
    a=input('Enter your course name')
    course.append(a)
    b=int(input('Enter your visa result'))
    visa.append(b)
    c=int(input('Enter your final result'))
    final.append(c)
    
for i in range(4): 
    average=(visa[i]/100*40)+(final[i]/100*60)
    if average<50:
        result.append("FAILED")
    elif average>=50:
        result.append("PASSED")

for i in range(4): 
    print("{}-- {}".format(course[i],result[i]))


# In[ ]:





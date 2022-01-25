#!/usr/bin/env python
# coding: utf-8

# In[86]:

#-------tersine cevirme--------#
list = [[1, 2], [3, 4], [5, 6, 7]]



# In[87]:


list.reverse()
list[0].reverse()
list[1].reverse()
list[2].reverse()


# In[82]:


list



#-------flatten seklinde gosterme------#

list = [["1",'a',['cat'],"2"],[[["3"]],'dog'],"4","5"]
flatlist=[]
for sublist in list:
    for element in sublist:
        flatlist.append(element)
print(flatlist)

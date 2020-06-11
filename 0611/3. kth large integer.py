#!/usr/bin/env python
# coding: utf-8

# In[2]:


n,k = map(int,input().split())
inpt = list(map(int, input().split()))
size = len(inpt)
l = []

for i in inpt:
    for j in inpt:
        for k in inpt:
            l += [i+j+k]
print(sorted(l)[-k])


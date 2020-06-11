#!/usr/bin/env python
# coding: utf-8

# In[13]:

#My code
T = int(input())
for test_case in range(1,T+1):
    n,s,e,k = map(int, input().split())
    inpt = list(map(int, input().split()))
    print('#%s %d' %(test_case,sorted(inpt)[k]))


# In[ ]:





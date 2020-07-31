#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 이분 검색
n,m = map(int, input().split())
a = list(map(int,input().split()))

# sorting
a.sort()

# binary search
start = 0 
end = len(a)-1

while start <= end:
    mid = (start+end)//2
    if a[mid] == m:
        print(mid+1) # index
        break
    elif a[mid] > m:
        end = mid-1
    else:
        start = mid+1


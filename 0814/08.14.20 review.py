#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1. 이분검색
n,m = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

start = 0
end = n-1

while start<=end:
    mid = (start+end)//2
    if l[mid]>m:
        end = mid-1
    elif l[mid]==m:
        print(mid+1)  # plus 
        break
    else:
        start = mid+1


# In[11]:


#2. 랜선자르기
def CountLines(length):
    cnt = 0
    for x in l:
        cnt += (x//length)
    return cnt

k,n = map(int, input().split())
l = []
res = 0
maximum = 0
for _ in range(k):
    tmp = int(input())
    l.append(tmp)
    if tmp > maximum: maximum = tmp
        
start = 1
end = sum(l)
res = 0

while start <= end:
    mid = (start+end)//2
    if CountLines(mid) >= n:
        res = mid
        start = mid+1
    else:
        end = mid-1
print(res)       


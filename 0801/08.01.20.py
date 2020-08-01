#!/usr/bin/env python
# coding: utf-8

# In[16]:


#2. 랜선 자르기

k,n = map(int,input().split())
l = []
res = 0
maximum = 0

# create a list and save given inputs to it
for i in range(k):
    tmp = int(input())
    l.append(tmp)
    maximum = max(res, tmp)

# create a fuction counting cuttable lines
def Count(len):
    cnt = 0
    for x in l:
        cnt += (x//len)
    return cnt

# binary search for the largest length
start = 1
end = maximum

while start<=end:
    mid = (start+end)//2
    if Count(mid)>=n:
        res = mid
        start = mid+1
    else:
        end = mid-1
print(res)


# In[17]:


#3. 뮤직비디오

n,m = map(int, input().split())
minutes = list(map(int, input().split()))

def Count(length):
    cnt = 1
    sum = 0
    for x in minutes:
        if mid >= maximum and sum + x > length:
            cnt += 1
            sum = x
        else:
            sum += x        
    return cnt

res = 0 
start = 0
end = sum(minutes)
maximum = max(minutes)

while start <= end:
    mid = (start+end)//2
    if Count(mid) >= m:
        res = mid
        end = mid-1
    else:
        start = mid+1
print(res)


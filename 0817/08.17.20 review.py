#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3. 뮤직비디오

n,m = map(int,input().split())
playtime = list(map(int,input().split()))

def CountDvds(len):
    cnt = 1
    sum = 0
    for x in playtime:
        if mid >= max_num and sum + x > len: #as cannot split a song into two cds
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

start = 0
end = sum(playtime)
max_num = max(playtime)
res= 0

while start<=end:
    mid = (start+end)//2
    if CountDvds(mid) <= m:
        res = mid
        end = mid-1
    else:
        start = mid+1
print(res)


# In[ ]:


#4. 마구간 정하기


n,c = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()

def CountDist(len):
    cnt = 1
    endpoint = l[0]
    for i in range(1,n):
        if l[i] - endpoint >= len:
            cnt += 1
            endpoint = l[i]
    return cnt

start = l[0]
end = l[-1]
while start<=end:
    mid = (start+end)//2
    if CountDist(mid) >= c:
        res = mid
        start = mid+1
    else:
        end = mid-1
print(res)


#!/usr/bin/env python
# coding: utf-8

# In[4]:


#4. 마굿간 정하기
n,c = map(int, input().split())

# create a list to save inputs
l = []
for _ in range(n):
    l.append(int(input()))
# sort the list
l.sort()

def Count(dist):
    cnt = 1
    endpoint = l[0]
    for i in range(1,n):
        if l[i] - endpoint >= dist:
            cnt += 1
            endpoint = l[i]
    return cnt 

start = l[0]
end = l[-1]
res = 0

while start <= end:
    mid = (start+end)//2
    if Count(mid)>= c:
        res = mid
        start = mid+1
    else:
        end = mid-1
print(res)


# In[28]:


#5. 회의실 배정
n = int(input())
meeting = []

#create a list to save inputs in tuple 
for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start,end))

#sort the list by the end time of each meeting
meeting.sort(key=lambda x: (x[1],x[0]))

#let's be greedy
endtime = 0
cnt = 0

for start, end in meeting:
    if start >= endtime:
        endtime = end
        cnt += 1
print(cnt)        


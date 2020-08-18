#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#5. 회의실 배정
n = int(input())
l = []
for _ in range(n):
    s,e = map(int,input().split())
    l.append((s,e))
l = sorted(l, key=lambda e: e[1])

cnt = 0
end = 0
for s, e in l:
    if s >= end:
        cnt += 1
        end = e
print(cnt)    


# In[ ]:


#6. 씨름 선수
n = int(input())
pi = []
for _ in range(n):
    h, w = map(int, input().split())
    pi.append((h,w))
pi.sort(reverse=True)

cnt = 0
max = 0

for h,w in pi:
    if w > max:
        cnt += 1
        max = w
print(cnt)


# In[31]:


#7. 창고 정리
n = int(input())
l = list(map(int, input().split()))
m = int(input())

l.sort(reverse=True)
for _ in range(m):
    l[0] -=1
    l[-1] +=1
    l.sort(reverse=True)
print(l[0]-l[-1])


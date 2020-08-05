#!/usr/bin/env python
# coding: utf-8

# In[2]:


#5. 씨름 선수
n = int(input())
l = []
for i in range(n):
    h,w = map(int, input().split())
    l.append((h,w))

# sort the list by height in descending order    
l.sort(reverse=True)

max = 0
cnt = 0
for height, weight in l:
    if weight > max: 
        max = weight
        cnt += 1        
print(cnt)


# In[23]:


#6. 창고 정리
l = int(input())
h = list(map(int,input().split()))
m = int(input())

h.sort(reverse=True)
for i in range(m):
    h[0] -= 1
    h[-1] += 1
    h.sort(reverse=True)
res = h[0] - h[-1]
print(res)


# In[32]:


#7. 침몰하는 타이타닉

n,m = map(int, input().split())
w = list(map(int, input().split()))

# sort the list by ascending order
w.sort()

cnt = 0
while w:            #cannot use for statement
    if len(w)==1:   #when only one person left
        cnt += 1
        break
    if w[0] + w[-1] > 140:
        w.pop()     #last person
        cnt += 1
    else:
        w.pop(0)    #first person
        w.pop()     #last person
        cnt += 1
print(cnt)       
#리스트 pop을 하면 각 element 순서를 앞으로 땡겨옴 => inefficient => use DEQUE

from collections import deque
w = deque(w)
while w:            #cannot use for statement
    if len(w)==1:   #when only one person left
        cnt += 1
        break
    if w[0] + w[-1] > 140:
        w.pop()     #last person
        cnt += 1
    else:
        w.popleft()    #first person
        w.pop()     #last person
        cnt += 1
print(cnt)


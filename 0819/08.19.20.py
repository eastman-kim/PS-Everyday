#!/usr/bin/env python
# coding: utf-8

# In[1]:


#7. 침몰하는 타이타닉

n,m = map(int, input().split())
w = list(map(int, input().split()))

w.sort()
cnt = 0

while w:
    if len(w)==1:
        cnt += 1
        break
    if w[0] + w[-1] > 140:
        cnt += 1
        w.pop()
    else:
        w.pop(0)
        w.pop()
        cnt += 1
print(cnt)


# In[14]:


#8. 증가수열 만들기

n = int(input())
l = list(map(int, input().split()))

left = 0
right = n-1
res = ""
tmp = []
last = 0

while left <= right:
    if l[left] > last: tmp.append((l[left],'L'))
    if l[right] > last: tmp.append((l[right],'R'))
    tmp.sort()
    if len(tmp) == 0: break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L': left += 1
        else: right -= 1
    tmp.clear()


# In[15]:





#!/usr/bin/env python
# coding: utf-8

# In[9]:


#9. 증가수열 만들기

n = int(input())
l = list(map(int, input().split()))

left = 0
right = n-1
res = ""
tmp = []
last = 0

while left<=right:
    if l[left] > last:
        tmp.append((l[left],'L'))
    if l[right] > last:
        tmp.append((l[right],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res = res+tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1]=='L':
            left += 1
        else:
            right -= 1
    tmp.clear()
print(len(res))
print(res)


# In[23]:


#10. 역수열 만들기 (다시!)
n = int(input())
l = list(map(int, input().split()))

seq = [0]*n

for i in range(n):
    for j in range(n):
        if l[i]==0 and seq[j]==0:
            seq[j] = i+1
            break
        elif seq[j]==0:
            l[i] -= 1            


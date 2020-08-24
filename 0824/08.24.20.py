#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#9.1 아나그램(리스트 해쉬)

s1 = input()
s2 = input()
l1 = [0]*52
l2 = [0]*52

for x in s1:
    if x.isupper():
        l1[ord(x)-65] += 1 # A ASCII CODE: 65
    else:
        l1[ord(x)-71] += 1 # a ASCII CODE: 97
for x in s2:
    if x.isupper():
        l2[ord(x)-65] += 1 # A ASCII CODE: 65
    else:
        l2[ord(x)-71] += 1 # a ASCII CODE: 97
        
for i in range(52):
    if l1[i] != l2[i]:
        print("NO")
        break
else: print("YES")


# In[ ]:


#10. 최소힙
import heapq 
a = []
while True:
    n = int(input())
    if n == -1: break
    if n == 0:
        if len(a) == 0: print(-1)
        else: print(heapq.heappop(a))
    else:
        heapq.heappush(a,n)


# In[ ]:


#11. 최대힙
import heapq
a = []
while True:
    n = int(input())
    if n == -1: break
    if n == 0: 
        if len(a) == 0: break
        else: print(-heapq.heappop(a))
    else:
        heapq.heappush(a,-n)


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#7. 교육과정 설계(큐)
from collections import deque
req = input()
n = int(input())

for i in range(n):
    curr = deque(req)
    plan = input()
    for x in plan:
        if x in curr:
            if x != curr.popleft():
                print("#%d NO" %(i+1)) #the order is not correct
                break
    else:
        if len(curr)==0:
            print('#%d YES' %(i+1))
        else:
            print("#%d NO" %(i+1))     #do not take all required courses


# In[ ]:


#8. 단어 찾기(해쉬)
n = int(input())
poem = dict()
for i in range(n):
    word = input()
    poem[word] = 1
for i in range(n-1):
    word = input()
    poem[word] = 0
for key,value in poem.items():
    if value == 1: 
        print(key)
        break


# In[ ]:


#9-1. 아나그램(딕셔너리 해쉬)
s1 = input()
s2 = input()
d1 = dict()
d2 = dict()

for x in s1:
    d1[x] = d1.get(x,0)+ 1
for y in s2:
    d2[y] = d2.get(y,0)+ 1
    
for i in d1.keys():
    if i in d2.keys():
        if d1[i] != d2[i]: 
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
            


# In[ ]:


#9-2. 아나그램(딕셔너리 해쉬)
s1 = input()
s2 = input()
dic = dict()

for x in s1:
    dic[x] = dic.get(x,0) + 1
for x in s2:
    dic[x] = dic.get(x,0) - 1
for x in s1:
    if dic.get(x) > 0:
        print("NO")
        break
    else:
        print("YES")


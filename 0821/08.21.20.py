#!/usr/bin/env python
# coding: utf-8

# In[1]:


#4. 후위 연산(스택)
a = input()
stack = []

for x in a:
    if x.isdigit():
        stack.append(int(x))
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if x == '+':  
            stack.append(num1+num2)
        elif x == '-':  
            stack.append(num1-num2)
        elif x == '*':  
            stack.append(num1*num2)
        elif x == '/':  
            stack.append(num1/num2)
print(stack[0])


# In[11]:


#5. 공주 구하기(큐)
from collections import deque

n,k = map(int, input().split())
a = deque(range(1,n+1))

while a:
    for _ in range(k-1):
        a.append(a.popleft())
    a.popleft()
    if len(a)==1:
        print(a[0])


# In[49]:


#6. 응급실(큐)
from collections import deque

n,m = map(int, input().split())
risk = [(pos, val) for pos,val in enumerate(list(map(int, input().split())))]
risk = deque(risk)

while True:
    tmp = risk.popleft()
    if any(tmp[1]<x[1] for x in risk):
        risk.append(tmp)
    else:
        cnt += 1
        if tmp[0]==m: break
print(cnt)        


# In[53]:





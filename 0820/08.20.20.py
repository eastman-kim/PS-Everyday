#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 가장 큰 수

num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0: stack[:-m]

res = ''.join(map(str,stack))    
print(res)


# In[43]:


#2. 쇠막대기
s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(': stack.append(s[i])
    else:
        if s[i-1] == '(':        #laser
            stack.pop()
            cnt += len(stack)
        else:                     #pipe
            stack.pop()
            cnt += 1
print(cnt)


# In[48]:


#3. 후위표기식
a = input()
stack = []
res = ''

for x in a:
    if x.isdigit(): res += x
    else:
        if x=='(': stack.append(x)
        elif x=='*' or x=='/': 
            while stack and (stack[-1]=='*' or stack[-1]=='/'): res += stack.pop() 
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(': res += stack.pop()
            stack.append(x)
        elif x==')': 
            while stack and stack[-1] != '(': res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)        


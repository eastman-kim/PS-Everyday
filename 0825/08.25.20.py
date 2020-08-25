#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1. 재귀함수를 이용한 이진수 출력

def recursive(x):
    if x == 0: return
    else: 
        recursive(x//2)
        print(x%2, end='')
        
n = int(input())
recursive(n)


# In[9]:


#2. 이진트리순회(DFS)
def DFS(n):
    if n>7: return
    else:
        print(n, end=' ') #전위순회
        DFS(n*2)
        DFS(n*2+1)
DFS(1)
print()
def DFS(n):
    if n>7: return
    else:
        DFS(n*2)
        print(n, end=' ') #중위순회
        DFS(n*2+1)
DFS(1) 
print()
def DFS(n):
    if n>7: return
    else:
        DFS(n*2)
        DFS(n*2+1)
        print(n, end=' ') #후위순회
DFS(1) 


#!/usr/bin/env python
# coding: utf-8

# In[13]:


#7. 사과나무

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

total = 0
start = end = n//2

for i in range(n):
    for j in range(start, end+1):
        total += grid[i][j]
    if i < n//2:
        start -= 1
        end  += 1
    else:
        start += 1
        end  -= 1


# In[15]:


#8. 모래시계

# create a grid
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

# rotate positions
m = int(input())
for i in range(m):
    row,direction,num = map(int, input().split())
    if direction == 0:  # go left
        for _ in range(num):
            g[row-1].append(g[row-1].pop(0))  # pop first & append last
    else:               # go right
        for _ in range(num):
            g[row-1].insert(0,g[row-1].pop()) # pop last & insert first
            
# sum crops           
start = 0
end = n-1
total = 0

for i in range(n):
    for j in range(start, end+1):
        total += g[i][j]
    if i<2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1


# In[72]:


#9. 봉우리 세기

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# add zeros to four sides
for i in range(n):
    g[i].append(0)           # to the right
    g[i].insert(0,0)         # to the left

g.insert(0,list([0]*(n+2)))  # to the top
g.append(list([0]*(n+2)))    # to the bottom

# count 봉우리
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(g[i][j] > g[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1


# In[ ]:





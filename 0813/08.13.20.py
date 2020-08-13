#!/usr/bin/env python
# coding: utf-8

# In[2]:


#5. 수들의 합

n,m = map(int, input().split())
l = list(map(int, input().split()))

left = 0
right = 1
sum = l[0]
cnt = 0

while True:
    if sum == m:
        cnt += 1
        sum -= l[left]
        left += 1
    elif sum > m:
        sum -= l[left]
        left += 1
    else:
        if right < n:
            sum += l[right]
            right += 1
        else:
            break
print(cnt)


# In[11]:


#6. 격자판 최대합

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
max = 0
#row
for i in range(n):
    row_tmp = col_tmp = 0
    for j in range(n):
        row_tmp += g[i][j]
        col_tmp += g[j][i]
        if row_tmp > max: max = row_tmp
        if col_tmp > max: max = col_tmp
            
#diagonal
left_tmp = right_tmp = 0
for i in range(n):
    left_tmp += g[i][i]
    right_tmp += g[n-i-1][n-i-1]
    if left_tmp > max: max = left_tmp
    if right_tmp > max: max = right_tmp
        
print(max)


# In[45]:


#7. 사과나무(다이아몬드)
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

start = end = n//2
total = 0
for i in range(n):
    for j in range(start, end+1):
        total += g[i][j]
    if i < n//2:
        start -=1
        end +=1
    else:
        start +=1
        end -= 1
print(total)


# In[68]:


#8. 곶감(모래시계)
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

#rotate the crops
m = int(input())
for _ in range(m):
    row, dir, mov = map(int, input().split())
    if dir == 0:  #go left
        for _ in range(mov):
            g[row-1].append(g[row-1].pop(0))
    elif dir == 1: #go right
        for _ in range(mov):
            g[row-1].insert(0, g[row-1].pop())

#sum crops up
start = 0
end = n-1
mid = n//2
total = 0

for i in range(n):
    for j in range(start, end+1):
        total += g[i][j]
    if i < mid:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(total)


# In[132]:


#9. 봉우리
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


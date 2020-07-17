#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 두 리스트 합치기 - 시간복잡도 nlogn
n1 = int(input())
l1 = list(map(int,input().split()))
n2 = int(input())
l2 = list(map(int,input().split()))
final = l1+l2
final.sort()
print(final)


# In[9]:


#1. 두 리스트 합치기 - 시간복잡도 n (이미 정렬된 리스트)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 비교
p1 = p2 = 0
c = []
while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n: c = c + a[p1:]
elif p2<m: c = c+ b[p2:]
for x in c:
    print(x, end=" ")   


# In[11]:


#2. 수의 합
n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
left = 0
right = 1
sum = a[0]

while True:
    if sum < m:
        if right < n:
            sum += a[right]
            right += 1
        else:
            break
    elif sum == m: 
        cnt += 1
        sum -= a[left]
        left +=1
    else:
        sum -= a[left]
        left += 1
print(cnt)


# In[24]:


# 격자판 최대합
n = int(input())
inpt = [list(map(int, input().split())) for _ in range(n)]
max = 0

#행,열
for i in range(n):
    row_sum = col_sum = 0
    for j in range(n):
        row_sum += inpt[i][j]
        col_sum += inpt[j][i]
    if max < row_sum: max = row_sum
    if max < col_sum: max = col_sum
        
#대각
diag_sum_left = diag_sum_right = 0
for i in range(n):
    diag_sum_left += inpt[i][i]
    diag_sum_right += inpt[i][n-i-1]
    if max < diag_sum_left: max = diag_sum_left
    if max < diag_sum_right: max = diag_sum_right
print(max)


# In[ ]:





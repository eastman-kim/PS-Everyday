#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1. 회문 문자열 검사

n = int(input())
for i in range(n):
    tmp = input().lower()
    m = len(tmp)
    for j in range(m//2):
        if tmp[j] != tmp[m-1-j]: 
            print("#%d NO" %(i+1))
            break
    else: print("#%d YES" %(i+1))


# In[23]:


#2. 숫자만 추출
# count the number of divisors
def countDivisor(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    return cnt

s = input()
tmp = ""

for x in s:
    if x.isdigit():
        tmp += x
res = int(tmp)

print(res)
print(countDivisor(res))


# In[43]:


#3. 카드 역배치
l = list(range(1,21))
for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        l[a+i-1], l[b-i-1] = l[b-i-1], l[a+i-1]
        
print(l)


# In[60]:


#4. 두 리스트 합치기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
res = []
# compare the values between a and b and add smaller one to the list.
# but it stops when one of lists has been added all without adding entire elements from two lists. 
while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        res.append(a[p1])
        p1 += 1
    else:
        res.append(b[p2])
        p2 += 1
# add rest of the elements to the list 
if p1 < n: res = res + a[p1:]
elif p2 < n: res = res + b[p2:]


# In[67]:


#5. 수들의 합
n,m = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
left = 0
right = 1
sum = l[0]

while True:
    if sum < m:
        if right < n:
            sum += l[right]
            right += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= l[left]
        left += 1
    else:
        sum -= l[left]
        left += 1


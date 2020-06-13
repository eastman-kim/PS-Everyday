#!/usr/bin/env python
# coding: utf-8

# # 0612 2nd Code Review
# `Copyright @ KOI`

# In[8]:


#1. kth divisor
n, k = map(int, input().split())
for i in range(1,k+1):        # 약수이므로 범위 1부터 n까지
    if n % i == 0 and i == k: # n의 약수이면서 k번째로 작은 수
        print(i)
        break
else: print(-1)               # 아니라면 -1 출력


# In[17]:


#2. kth small number
T = int(input())
for test_case in range(1,T+1):
    n,s,e,k = map(int, input().split())
    l = list(map(int, input().split()))
    l = l[s-1:e]     # l s번째 부터 e번째까지 슬라이싱
    l.sort()         # k번째로 작은 수 구하기 위해 오름차순 정렬
    print('#%s %d' %(test_case,l[k-1]))    # 슬라이싱한 리스트이 k번째 수


# In[32]:


#3. kth large number
n, k = map(int, input().split())
l = list(map(int, input().split()))

s = set()                    # 중복된 수가 나올 경우를 제거해야 하므로 set를 만든다
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            s.add(l[i]+l[j]+l[m])
newlist = list(s)            # 정렬을 해야하므로 set을 list로 변경
newlist.sort(reverse=True)   # 내림차순 정렬
print(newlist[k-1])          # k번째 큰 수 출력


# In[54]:


#4. mean
n = int(input())
l = list(map(int, input().split()))

avg = int(round(sum(l)/n,0)) # 소수 첫째 자리에서 반올림. 
min =  9999999
for idx,x in enumerate(l): 
    dist = abs(x-avg)        # 거리이므로 절댓값
    if dist < min:           
        min = dist
        index = idx +1       # enumerate 인덱스 0부터 시작. k번째이므로 +1
        score = x
    elif dist == min:
        if score < x:
            score = x
            index = idx +1
print(avg,index)


# In[4]:


#5. Polyhedron
n,m = map(int,input().split())
tbl = [0]*(n+m+1)            #cnt 기록할 table 생성

for i in range(1,n+1):       #정육면체이므로 1부터 n까지
    for j in range(1,m+1):   
        tbl[i+j] += 1      

for i in range(len(tbl)):
    if tbl[i] == max(tbl):   
        print(i, end=' ')


# In[9]:


#6. digit sum
def digit_sum(x):
    sum = 0
    while x>0:
        tmp = x%10
        sum += tmp
        x = x//10
    return sum

n = int(input())
l = list(map(int, input().split()))

max = 0
for x in l:
    sum = digit_sum(x)
    if max < sum:
        max = sum
        outp = x
print(outp)


# In[49]:


#7. prime number
n = int(input())
tbl = [0]*(n+1)
cnt = 0
for i in range(2,n):           # 2부터 시작
    if tbl[i]==0:
        cnt += 1
        for j in range(i,n,i): # i의 배수 1로 만들어 주기
            tbl[j]=1
print(cnt)


# In[50]:


#8.  flipped prime number
def reverse(x):
    rev = 0
    while x>0:
        t = x%10
        x = x//10
        rev = rev*10+t   
    return rev

def isPrime(x):
    if x<2: return False
    for i in range(2,x//2+1):   # 첫 소수인 2 때문에 절반만 돌아도 소수인지 알 수 있음
        if x%i==0: return False
    return True    

n = int(input())
l = list(map(int,input().split()))

for x in l:
    res = reverse(x)
    if isPrime(res): print(res, end=' ')


# In[60]:


#9. dice game
n = int(input())
max = 0

for i in range(n):
    tmp = list(map(int,input().split()))      # 리스트로 받아서 정렬하면 아래에서 가장 큰 수를 찾기 수월하다
    tmp.sort()
    d1,d2,d3 = tmp
    
    if d1==d2 and d2==d3: sum = 10000+d1*1000 # 세 개의 숫자가 같을 때
    elif d1==d2 or d1==d3: sum = 1000+d1*100  # 두 개의 숫자가 같을 때
    elif d2==d3: sum = 1000+d2*100            # 두 개의 숫자가 같을 때
    else: sum = d3*100                        # 하나도 같지 않을 때
    
    if sum>max:
        max = sum
print(max)


# In[67]:


#10. grading
n = int(input())
l = list(map(int, input().split()))
cnt = sum = 0

for i in range(n):
    if l[i]==1: 
        cnt += 1
        sum += cnt
    else: cnt=0
print(sum)


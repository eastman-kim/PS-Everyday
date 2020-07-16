#!/usr/bin/env python
# coding: utf-8

# Problem sets copyright @ Korean Olympiad in Informatics, KOI

# In[11]:


#1.회문 문자열

n = int(input())
for i in range(n):
    s = input()
    s = s.upper() # Capitalize the given string
    size = len(s)
    
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('#%d NO' %(i+1))
            break
    else: print('#%d YES' %(i+1))


# In[9]:


#1. 회문 문자열 - Make it pythonic
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() 
    size = len(s)
    
    if s != s[::-1]: print('#%d NO' %(i+1))
    else: print('#%d YES' %(i+1))


# In[48]:


#2. 숫자만 추출 문제
s = input()
tmp =''

#숫자인지 확인
for x in s: 
    if x.isdigit(): tmp += x
num = int(tmp)

#약수 개수 구하기
cnt = 0
for i in range(1,num+1):
    if num%i==0: cnt+=1
print(cnt)


# In[45]:


#2. 숫자만 추출 문제 - Str 변환 없이 풀기
s = input()
res = 0

for x in s: 
    if x.isdigit(): res = res*10 + int(x)

cnt = 0
for i in range(1,res+1):
    if res%i ==0: cnt+=1
print(cnt)


# In[66]:


#3 .카드 역배치
#20까지 카드 리스트 만들기
l = [0]* 20
for i in range(len(l)):
    l[i] = i+1

#카드 배치 바꾸기
for _ in range(10): # 10 ranges will be given
    a,b = map(int, input().split())
    for i in range((b-a+1)//2):
        l[a+i-1], l[b-i-1] = l[b-i-1], l[a+i-1] #swaping cards

#리스트 출력
for x in l:
    print(x, end=' ')


# In[73]:


#3. 카드 역배치 - range 0부터 시작하고 나중에 0 pop하기
#20까지 카드 리스트 만들기
l = list(range(21))

#카드 배치 바꾸기
for _ in range(10):
    a,b = map(int, input().split())
    for i in range((b-a+1)//2):
        l[a+i], l[b-i] = l[b-i],l[a+i]

#리스트 출력
l.pop(0) #remove 0        
for x in l:
    print(x, end=' ')


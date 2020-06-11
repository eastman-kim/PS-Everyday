#!/usr/bin/env python
# coding: utf-8

# ### Section 2
# #### K번째 약수

#My Code - Time Limit!!!
n, k = map(int, input().split())
l = []
for num in range(1,n+1):
    if n%num==0: l.append(num)
if len(l)<k: print(-1)
else: print(l[k-1])


#Solution
n, k = map(int, input().split())
cnt = 0
for i in range(1,n+1):
    if n%i==0: cnt += 1
    if cnt==k: 
        print(i)
        break
else: print(-1)





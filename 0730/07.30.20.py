#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#10. 스도쿠 검사

def check(g):
    # row, column check list
    for i in range(9):
        chklst_row = [0]*10
        chklst_col = [0]*10
        for j in range(9):
            chklst_row[g[i][j]]=1
            chklst_col[g[j][i]]=1
        if sum(chklst_row) != 9 or sum(chklst_col) != 9:
            return False
    # group check list
    for i in range(3):
        for j in range(3):
            chklst_grp = [0]*10
            for k in range(3):
                for s in range(3):
                    chklst_grp[g[i*3+k][j*3+s]]=1
            if sum(chklst_grp) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a): print('YES')
else: print('NO')


# In[8]:


#11. 격자판 회문수

g = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
# row check
for i in range(3):
    for j in range(7):
        tmp = g[j][i:i+5]
        if tmp == tmp[::-1]: 
            cnt += 1
        # column check
        for k in range(2):
            if g[i+k][j] != g[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)


#N 이상 M 이하
#1,000,000이하의 수

import math

chkFlag=[True]*1000001

M,N=map(int, input().split())

for i in range(2,int(math.sqrt(N))+1):
    if chkFlag[i]==True:
        j=2
        while i*j <=N:
            chkFlag[i*j]=False
            j+=1

for i in range(M, N+1):
    if chkFlag[i]==True:
        print(i)



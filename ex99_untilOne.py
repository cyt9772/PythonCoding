N,K=map(int, input().split(' '))

cnt=0

while True:
    if N%K==0:
        N=N//K
        cnt+=1
    else:
        cnt+=N%K
        N=N-N%K

        if N==0:
            break
    if N==1:
        break

print(cnt)
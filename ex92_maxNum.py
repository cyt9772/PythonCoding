#N: 입력 data개수, M: 덧셈의 개수, K: 더하기 제한
N,M,K=map(int, input().split(' '))
data=list(map(int, input().split(' ')))
data.sort(reverse=True)

#data[0] 제일 큰 수, data[1] 두번째 큰 수
set_plus=data[0]*K+data[1]
m=M//(K+1)
n=M%(K+1)

#나머지 계산
rem=data[0]*n

#가장큰수
res=set_plus*m + rem

print(res)

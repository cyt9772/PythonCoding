#N: 입력 data개수, M: 덧셈의 개수, K: 더하기 제한
N,M=map(int, input().split(' '))

maxValue=0

for i in range(N):
    data=list(map(int, input().split(' ')))
    maxValue=max(maxValue, min(data))

print(maxValue)

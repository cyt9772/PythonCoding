n=int(input())

data=[0]*30001

for i in range(2, n+1):
    data[i]=data[i-1]+1 #1 연산

    if i%2==0:
        data[i]=min(data[i], data[i//2]+1) #2로 나누기
    if i%3==0:
        data[i]=min(data[i], data[i // 3] + 1) #3으로 나누기
    if i%5==0:
        data[i]=min(data[i], data[i // 5] + 1) #5로 나누기

print(data[n])

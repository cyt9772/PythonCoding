n=int(input())
stock=list(map(int, input().split()))

data=[0]*(n+1)
data[1]=stock[0]
data[2]=max(stock[0], stock[1])

for i in range(3, n+1):
    data[i]=max(data[i-1], data[i-2]+stock[i-1])

print(data[n])


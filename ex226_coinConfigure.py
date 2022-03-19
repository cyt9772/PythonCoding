n, target=map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
coins.sort()

data=[10001]*(target+1)
data[0]=0

for coin in coins:
    for i in range(1,10001):
        if i >=target+1:
            break
        else:
            if data[i-coin] !=10001:
                data[i]=min(data[i], data[i-coin]+1)
if data[n]==10001:
    print("-1")
else:
    print(data[target])

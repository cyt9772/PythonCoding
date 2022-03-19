n=int(input())

data=[0]*(n+1)

data[1]=1
data[2]=3

for i in range(3,n+1):
    data[i]=(data[i-1]+2*data[i-2])%796796

print(data[n])


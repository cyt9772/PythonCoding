n=5
data=[10,20,30,40,50]

subtotal=[0]*(n+1)

for i in range(1,n+1):
    subtotal[i] = subtotal[i-1] + data[i-1]

print(subtotal)

#3~4 구간합
print(subtotal[4] - subtotal[2])
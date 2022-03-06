n=int(input()) # 데이터 개수
m=int(input()) # 부분합
data=[1,2,3,2,5]

count=0
start=0
end=0

subTotal=data[start]

while start<n:
    if subTotal < m:
        if end < n:
            end +=1
        subTotal +=data[end]
    elif subTotal >m:
        subTotal -=data[start]
        start +=1
    elif subTotal == m:
        count +=1
        subTotal -=data[start]
        start +=1

print(count)








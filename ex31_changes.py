m=int(input()) # changes

coins=[500,100,50,10]

cnt=0 #동전개수
rem=m

for coin in coins:
    cnt +=(rem//coin)
    rem =rem%coin

print(cnt)
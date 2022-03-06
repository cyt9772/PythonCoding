from itertools import combinations

r,n=map(int, input().split(' '))
data=input().split(' ')
vowels=['a','e','i','o','u']

#data=['a','t','c','i','s','w']
data.sort()

#print(data)

for passwd in combinations(data,r):
#    print('Passwd', passwd)
    cnt=0;
    for x in passwd:
        if x in vowels:
            cnt +=1
    if 1<=cnt<=(r-2):
        print("".join(passwd))
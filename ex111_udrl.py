N=int(input())
data=list(input().split(' '))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

move_types=['L','R','U','D']
x=1
y=1

for plan in data:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    if nx>N or nx <1 or ny>N or ny <1:
        continue
    x,y=nx,ny

print(x,y)


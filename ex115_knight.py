pos=input()
y=ord(pos[0])-ord('a')+1
x=int(pos[1])

cnt=0
dx=[-2, -1, -1, -2, 2, 1, 1, 2]
dy=[-1, -2,  2,  1, 1, 2,-2,-1]

for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>8 or nx<1 or ny>8 or ny<1:
        continue;
    cnt+=1

print(cnt)
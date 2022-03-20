import heapq, sys
input=sys.stdin.readline
INF=int(1e9)

n,m =map(int, input().split()) #노드/간선의 개수
start=int(input()) #start node

#노드 정보 담는 graph를 node 개수 만큼 정리
graph=[ [] for i in range(n+1)]

#거리값을 INF로 초기화
distance=[INF]*(n+1)

#간선정보 입력 받기
for i in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(n+1):
    if distance[i]==INF:
        print("INFINFTY")
    else:
        print(distance[i])
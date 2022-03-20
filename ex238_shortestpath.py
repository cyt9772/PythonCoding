import sys
INF=int(1e9)

n,m =map(int, input().split()) #노드/간선의 개수
start=int(input()) #start node

#노드 정보 담는 graph를 node 개수 만큼 정리
graph=[ [] for i in range(n+1)]

#방문 여부 check
visited=[False]*(n+1)

#거리값을 INF로 초기화
distance=[INF]*(n+1)

#간선정보 입력 받기
for i in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    node=0

    for i in range(1, n+1):
        if distance[i] < min_value and visited[i]==False:
            min_value=distance[i]
            node=i

    return node

def dijkstra(start):
    distance[start]=0
    visited[start]=True

    #그래프로부터 각 노드까지 거리값을 가져와서 대입
    for j in graph[start]:
        distance[j[0]]=j[1]

    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True

        for j in graph[now]:
            cost=distance[now]+j[1]

            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

for i in range(n+1):
    if distance[i]==INF:
        print("INFINFTY")
    else:
        print(distance[i])

    





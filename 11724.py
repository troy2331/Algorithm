# 백준 11724 연결요소의 개수
# 방향없는 그래프가 주어졌을 때, 연결요소의 개수를 구해라
# 첫째줄 정점N, 간선M , 둘째줄부터 M개의 간선의 양 끝점 u,v
# 연결요소란 몇 뭉텅이인지를 뜻함
# a에방문하면, a와 연결된것들을 방문해야됨, 큐를 이용해야될것같음
import sys
sys.setrecursionlimit(10000)
from collections import deque

input = sys.stdin.readline
Edge = deque([])

N, M = map(int, input().split())
visited = [False for _ in range(N+1)] # 0리스트
graph = [[] for _ in range(N+1)]
graph[0] = [0,0]
count = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

def DFS(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)
for i in range(1, len(visited)):
    if visited[i] == 0:
        count += 1
        DFS(graph, i, visited)

print(count)
#재귀적으로 하니 속도 측면에서 안좋음
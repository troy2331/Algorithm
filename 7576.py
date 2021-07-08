# 백준 7576번 토마토
# bfs처럼 익은토마토 옆 하루지나면 익게됨, 다익으려면 얼마나 걸리는지를 구해라
# 익은게1, 안익은게0, 비어있는게-1
# 만약 이미 모두익어잇으면 0일, 모두익지못할상황이면 -1

# 풀이 일단 BFS탐색을 써야하고, 1을기준으로 모든것이 동시에 BFS해야함
# 탐색을 마친 후, 0이 남아있다면 -1
# 따라서 queue에다가 1의 좌표를 다 넣어주고, 뺄떄마다 BFS 탐색

'''
M, N = map(int, input().split())
List = []
for i in range(N):
    List.append(list(map(int, input().split())))

a = [-1,1,0,0]
b = [0,0,-1,1]

queue = []

for j in range(N):
    for k in range(M):
        if List[N][M] == 1:
            queue'''

from collections import deque #덱 라이브러리
m, n = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(map(int, input().split())))
def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
                s[x][y] = s[a][b] + 1
                queue.append([x, y])
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])
bfs()

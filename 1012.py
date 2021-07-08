# 백준 1012 유기농배추
# 0배추x 1배추o
# 입력 테스트케이스갯수T, 가로M 세로N, 배추위치개수, 위치좌표
# 지렁이 배추이동가능, 즉 뭉텅이 갯수 세라는 뜻
import sys
from collections import deque
input = sys.stdin.readline

Solution = []
T = int(input())
BaeChu = deque([])
Queue = deque([])
count = 0

a = [-1,1,0,0]
b = [0,0,-1,1]

for i in range(T):
    M, N, K = map(int, input().split())
    map1 = [[0 for col in range(M)] for row in range(N)]
    for j in range(K):
        BaeChu.append(list(map(int, input().split())))
        x = BaeChu[j][1]
        y = BaeChu[j][0]
        map1[x][y] = 1 #배추맵완성
    for ii in range(N):
        for jj in range(M):
            if map1[ii][jj] == 1:
                Queue.append([ii,jj])
                map1[ii][jj] = -1
                count += 1
            while Queue:
                t = Queue.popleft()
                dx = t[0]
                dy = t[1]
                for kk in range(4):
                    xx = dx + a[kk]
                    yy = dy + b[kk]
                    if 0<=xx<=N-1 and 0<=yy<=M-1:
                        if map1[xx][yy] == 1:
                            Queue.append([xx,yy])
                            map1[xx][yy] = -1
                        else:
                            continue
                    else:
                        continue
    Solution.append(count)
    BaeChu = deque([])
    Queue = deque([])
    count = 0

for m in range(len(Solution)):
    print(Solution.pop(0))






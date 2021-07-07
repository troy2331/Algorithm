#2178 미로찾기
# 1이이동가능, 0벽 1,1에서 출발할때 NM으로 가기위한 최소칸수
# BFS활용하여 한칸갈때마다 1씩늘려서 체크하면될듯
'''
import sys
input = sys.stdin.readline
a = [-1,1,0,0]
b = [0,0,-1,1]

#list = []
x, y = list(map(int, input().split()))
#for i in range(x):

array = [[0 for col in range(y)] for row in range(x)]
for i in range(x):
    array[i] = input()

count = 1
aa = 0
bb = 0
queue = []
while True:
    count += 1
    for i in range(4):
        a1 = aa + a[i]
        b1 = bb + b[i]
        if a1 < 0 or b1 < 0 :
            continue

        elif a1 == x and b1 == y:
            return count

        elif array[a1][b1] == 1:
            array[a1][b1] = count
            queue.append([a1,b1])
    t = queue.pop(0)
    aa = t[0]
    bb = t[1]
    if aa == x and bb = y:
        break

print(count)
'''
n,m = map(int, input().split())
s = []
queue = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    s.append(list(input()))
queue = [[0,0]]
s[0][0] = 1
while queue:
    a,b = queue[0][0], queue[0][1]
    del queue[0]
    for j in range(4):
        x = a+dx[j]
        y = b+dy[j]
        if 0<=x<n and 0<=y<m and s[x][y] =='1':
            queue.append([x,y])
            s[x][y] = s[a][b] + 1
print(s[n-1][m-1])
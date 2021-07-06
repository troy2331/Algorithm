a,b,c = map(int, input().split())
s = [[0] * (a+1) for i in range(a+1)]# 4,5,1 -> 5*5 0행렬

visit = [0 for i in range(a+1)] #visit는 0 (a+1)만큼
for i in range(b):
    x,y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, a+1):
        if visit[i] == 0 and s[v][i] == 1: #visit이 아직 비엇고
            #특정 s[v][i]==1이라면 들어가서 재귀호출.
            dfs(i)

def bfs(v):
    queue = [v] #리스트에 시작점
    visit[v] = 0 #시작점의인덱스를 0으로
    while(queue): #큐가 존재하면 반복
        v=queue[0] #시작점 할당
        print(v, end=' ') #v출력 시작점일단
        del queue[0] # 썻으면 지움
        for i in range(1, a+1): # 정점횟수만큼 반복
            if visit[i]==1 and s[v][i] == 1: # 둘다1일때  queue에추가
                queue.append(i)
                visit[i]=0
dfs(c)
print()
bfs(c)
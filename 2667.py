# 백준 2667 단지번호붙이기
# 1이 집, 좌우,위아래 붙어있으면 같은단지, 지도크기를 입력받고 단지의 각각의 갯수를 출력
# Naive한 풀이는, (0,0)부터 1이면, 탐색으로 1들을 count하면서 세고, 더이상 갈곳이 없으면
# 넘어가는것이다.
# 1이면, count하며 한칸씩이동탐색, 탐색한곳은 -1할당, 더이상 탐색이 끝나면 다음으로 이동


N = int(input())
A = []
for i in range(N):
    A.append(list(input()))

a = [1,-1,0,0]
b = [0,0,-1,1]
queue = []
count = 0
Coun=[]

for i in range(N):
    for j in range(N):
        if A[i][j] == '1':
            queue.append((i,j))
            A[i][j] = '-1'
            count += 1
        while queue:
            t = queue.pop(0)
            x = t[0]
            y = t[1]
            for k in range(4):
                aa = x + a[k]
                bb = y + b[k]
                if 0 <= aa < N and 0 <= bb < N:
                    if A[aa][bb] == '1':
                        count += 1
                        A[aa][bb] = '-1'
                        queue.append([aa, bb])
                else:
                    continue
        Coun.append(count)
        count=0

X = sorted(Coun)
while X[0] == 0:
    X.pop(0)
print(len(X))
for i in range(len(X)):
    print(X.pop(0))
# 여기까지가 내 코드, 정답
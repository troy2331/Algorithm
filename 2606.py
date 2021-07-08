# 백준 2606 바이러스
# 입력:컴퓨터수 100이하, 그다음 연결되어있는 컴퓨터쌍 ex( 1 5 )
# 출력:1번컴퓨터가 바이러스 걸리면 몇개가 걸리는지
# 1 2라면, 2랑연결되어있는, 2 3 , 3과연결되어있는  ...
# 첫째줄 - 점갯수, 둘째줄 - 줄갯수 셋째~ - 연결쌍 a b
'''
N = int(input())
M = int(input())
S = []
for i in range(M):
    S.append(list(map(int, input().split())))
print(S)

# 방문한거 다 넣고 중복제거하면 되지 않을까?
# t = sorted(t, key=lambda t: (t[1], t[0])) 튜플정렬하는거 외우자
Sort = sorted(S, key=lambda S: (S[0], S[1]))
print(Sort)

One = [0]*100

for j in range(M):
    if Sort[j][0] == 1:
        One[j] = Sort[j][1]


'''

Dict={}
for i in range(int(input())):
    Dict[i+1] = set()
for j in range(int(input())):
    a, b = map(int, input().split())
    Dict[a].add(b)
    Dict[b].add(a)

def dfs(start, Dict):
    for i in Dict[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, Dict)
visited = []
dfs(1, Dict)
print(len(visited)-1)
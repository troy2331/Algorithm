# 숫자카드게임, 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
B = []
answer = 0
for j in range(N):
    answer = A[j][0]
    for k in range(M):
        if A[j][k] < answer:
            answer = A[j][k]
    B.append(answer)
B.sort()
print(B.pop())

# 여기까지가 내 풀이, 맞았지만 책에선 훨씬 간단하게 풀었다, min() 메소드를 이용한 풀이다.

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    result = max(result, min_value)

print(result )
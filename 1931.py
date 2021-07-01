# 최대 회의 갯수 찾기
# (회의시작시간, 회의마치는시간) 을 입력으로 받음
# 따라서, 회의마치는시간을 기준으로 정렬한 뒤에, for문을 사용해 구했음

TimeList = []

N = int(input())
for i in range(N):
    TimeList.append(list(map(int, input().split())))

count = 1

t = TimeList
t = sorted(t, key=lambda t: (t[1], t[0]))  # 마감 시간을 기준으로 정렬
A = t[0]

for i in range(N-1):
    if A[1] <= t[i+1][0] :#끝나있다면
        count += 1
        A = t[i+1]
    else:
        continue

print(count)


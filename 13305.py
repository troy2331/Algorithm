# 그리디알고리즘 백준13305 주유소
# N개의도시, 각도시 기름가격, 이동km // 최소비용 구하기

N = int(input()) # 도시 개수
Path = []
Price = []

Path.append(list(map(int, input().split()))) # N-1개
Price.append(list(map(int, input().split()))) # N개

Path = Path[0]
Price = Price[0]
# 약간 정렬과 비슷한 느낌인것 같다.
# 제일 싼 곳을 찾고, 그보다 오른쪽의 총 Path만큼 주유

Min = Price[0]
sum = 0
for i in range(N-1):
    if Min > Price[i]:
        Min = Price[i]
    sum += (Min * Path[i])
print(sum)


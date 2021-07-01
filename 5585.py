# 백준 5585 거스름돈
# 가격 1~1000 입력을받고
# 1000엔지폐를 냈을때 거스름돈의 최소갯수

N = int(input())
n= 1000-N
A = [500, 100, 50, 10, 5, 1]
count = 0
for i in range(6):
    count += (n//int(A[i])) #몫
    n = (n%int(A[i])) #나머지
    if n == 0:
        break
print(count)
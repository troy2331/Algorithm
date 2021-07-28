# N이 1이될때까지의 최소의 횟수, 1번은 -1, 2번은 K로나누기
# N=17, K=4라면, 17-16-4-1 총 3회 필요

N, K = map(int, input().split())
count = 0
while True:
    if N == 1:
        print(count)
        break
    elif N%K == 0:
        count += 1
        N = N/K
    elif N%K != 0:
        count +=1
        N -= 1
    elif 1 < N < K:
        count += 1
        N -= 1

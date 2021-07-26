# 큰수의법칙, 주어진수를 M번 더하여 가장 큰 수를 만드는 법칙
# 2,4,5,4,6 에 M이 8이고, K가 3이라면, 66656665 = 46

N, M, K = map(int, input().split())
A = []
A.append(input().split())
A = A[0]
A.sort(reverse=True)
Now = 0
count = 0
sum = 0
k = 0
for i in range(M):
    if count < K:
       sum += int(A[Now])
       count += 1
    else :
        Now += 1
        sum += int(A[Now])
        k += (count+1)
        count = 0
        Now = 0
print(sum)

# 나는 위와같이 답을 도출하였다.  책에나온 풀이와 비교해보자
'''
n,m,k = map(int, input().split())
data = list(map(int, input().split())

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
책에서는, 젤큰수, 그다음큰수 2개만필요하기 때문에 두개만 빼서 이용했다. 

시간복잡도를 줄이는 방법도 나와있었다. 반복되는 수열에 대해서, 첫번째로큰수 + 작은수한번 더해질 때 
K+1개가 반복되는 수열이 나타나는 규칙이 생긴다. 이렇게 개선한 코드는 다음과 같다. 

n,m,k = map(int, input().split())
data = list(map(int, input().split())

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
'''


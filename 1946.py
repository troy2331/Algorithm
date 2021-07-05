# 지원자의 숫자 N, 그뒤 각각의 서류등수, 면접등수
# 어느지원자의 모든 지원자와 비교하는데하 나라도 밀리지 않아야 뽑힐수있음.
# 1등 지원자보다, 둘다떨어지면 제외
# naive하게 생각하면, 각각의 요소랑 모두 비교하여 +=1 하는것인데 이건 아닐거같다.
# 규칙이뭘까.... 정렬한다하더라도 예외가 있다.
# [0]의 1등의 반대보다 큰것 제외 and [1] 1등의 반대([0])값보다 큰것들 제외한 카운트

N = int(input())
A = []
B = []
for i in range(N):
    Num = int(input())
    for j in range(Num):
        A.append(list(map(int, input().split())))
    t = sorted(A, key = lambda A: (A[1], A[0])) #뒤꺼오름차순
    A.sort()
    count = Num
    for k in A:
        if int(k[0]) > int(t[0][0]):
            count -= 1
        elif int(k[1]) > int(A[0][1]):
            count -= 1
        else:
            continue
    B.append(count)
    A = []
for i in range(N):
    print(B[i])

# 모범답안, 위에 시간초과떠서 불통과했음
# a,b = map(int, input(),split()) 으로 받고
# 기존에 0으로 만들어놓은 배열에, 인덱스1, 4-> 이런식으로 표현하는방법 기억하자.
import sys
input = sys.stdin.readline
x = int(input())
for i in range(x):
    n = int(input())
    s = [0 for i in range(n+1)] # 0짜리 배열만들기
    for j in range(n):
        a,b = map(int, input().split())
        s[a] = b
    min_n = s[1]
    cnt = 0
    for k in range(2, n+1):
        if s[k] > min_n:
            cnt += 1
        else:
            min_n = s[k]
    print(n-cnt)

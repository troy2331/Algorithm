# 백준 그리디알고리즘 4796 캠핑
# 캠핑장을 연속하는 P일중 L일동안 사용가능, V일짜리 휴가시작
# L, P, V ,입력 -> 며칠?
import sys
input = sys.stdin.readline
L, P, V = map(int, input().split())

count = 0
count2 = 0
answer = 0
sol = 0
#두가지 케이스, 1.
while count2 < V:
    count += 1
    count2 += 1
    if answer < L:
        answer += 1
    elif count == P:
        sol += answer
        count = 0
        answer = 0
sol += answer
if sol != 0:
    print("Case 1: ",sol)

#방법은 맞았지만 시간초과가 떳다.

#휴가의 v일 중 (v//p)만큼 , V%P를, 그리디 알고리즘에선 나머지와 몫으로 할 방법을 먼저 생각해야겠다.
#반성하자
import sys

i = 1
while True:
    L, P, V = map(int, input().split())
    if L+P+V == 0:
         break
    sol = (V//P)*L # ex 20//8=2 * L
    sol += min((V%P), L) # 나머지 V%P = 나머지4중에, L보다 작은것 고르면 됨
    print("Case %d: %d" %(i, sol))
    i += 1
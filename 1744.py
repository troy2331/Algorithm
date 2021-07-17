# 백준 그리디알고리즘 1744 수 묶기
# 길이가 N인 수열, 수열의합
# 입력 4 / -1,2,1,3 -> 최대가나오게끔 -1+1+(2*3) 이런식으로 묶기
from collections import deque
import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()
A = deque(A)
# 정렬을 시킨 후 , pop하면서 1보다 클경우에 2개씩 곱해주고, 1이나오면 다그냥 더해줌
count = 0
while len(A) >= 2 and A[0] <= 0 and A[1] <= 0:
    D = A.popleft()
    E = A.popleft()
    count += (D * E)
    if len(A) < 2:
        break
while A:
    B = A.pop()
    if len(A) == 0:
        count += B
        break
    elif B > 1:
        C = A.pop()
        if C > 1:
            count += (B*C)
        else:
            count += B
            count += C
            while A:
                count += A.pop()
    else:
        count += B
        while A:
            count += A.pop()
print(count)

# 음수끼리 곱하면 +가 된다는 것을 망각해서 계속 틀렸다고 판정이 되었다.
# 음수끼리 곱하는것도 처리를 해보자.
# 반례1 - 음수만있을떄
# 반례2 - 음수+0이있을때, -1*0 -> 0으로 처리해야됨
# 그래서 다시 구현했는데, Test case는 모두 만족했지만
# 런타임에러가 떳다.
# 1,0 을 입력했을때, 오류가 생겨 런타임에러오류가 떳다. 0하나만 입력했을때를 처리하기 위해서
# len(A) >= 2 조건을 추가했더니 정답처리가 되었다.
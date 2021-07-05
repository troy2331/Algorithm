# 백준 2217번 로프
# k개의 로프를 사용, w중량 들어올리면 각각 w/k중량 걸림
# 최대중량을 구하는 프로그램
# 2개, 10,15면, 최대중량 20을들수잇음
# 만약, 2개, 1,15라면, 15하나만써서 15키로드는게 나을것임
# 3개 1,1,15라면, 15하나로 15드는게 나을것임,
# 따라서, 추론할수있는것은 정렬한후, 최댓값, 그다음값*2, 그다음값*3... 초기화
# 10,10,5 -> 20 , 5,10,15 -> 15, 5,10,15,20 -> 35

N = int(input())
A = []
B = []
for i in range(N):
    A.append(int(input()))
A.sort()
i = 0
j = 0
Num = A[len(A)-1]
for i in range(1, len(A)):
    j+=1
    if Num <= (j+1)*A[-1-i]:
        Num = (j+1)*A[-i-1]
    else:
        continue
print(Num)
#맞았는데 시간이 너무 오래걸렸다. 다른사람의답안과 복잡도차이가 어디서 나는지 확인해봐야겠다
'''
import sys
In = sys.stdin.readline

def main():
    n = int(In()) #인풋으로 받고 
    rope = [0] * 10001 # 배열 초기화 
    for _ in range(n): # n번반복 
        rope[int(In())] += 1  # k인풋받기
    m, s = 0, 0
    for x in range(10000,-1,-1): # 뒤로시작
        s += rope[x] # 
        m = max(m, x * s)
    print(m)
main()
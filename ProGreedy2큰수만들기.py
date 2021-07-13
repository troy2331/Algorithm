'''문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.'''

def solution(number, k):
    answer = ''
    # 젤 작은숫자부터 K개 제거하고, 순서는 그대로 출력하면 됨
    A = []
    C = []
    for i in range(len(number)):
        A.append(number[i])
    C = sorted(A)
    for j in range(k): # k 번 제거하자
        B = C.pop(0)
        for m in range(len(A)):
            if A[m] == B:
                A.pop(m)
                break
            else:
                continue
    for _ in A:
        answer += _

    return answer

#예외가 생겼다. 4177252841 -> 775841나와야하는데 작은것만 빠졋다.

#다시 생각해보면, 먼저 number에 k index값까지의 젤 큰수를 제외하고 지우는게 1순위
#그 다음은, 작은숫자를 그냥 지우면 된다.

# 모범답안으로 스택을 이용하여 진행했다.

def solution(number, k):
    stack = [number[0]] # 스택에 초기값 1234면, 1이 들어가있음
    for num in number[1:]: # 234들에대하여
        while len(stack) > 0 and stack[-1] < num and k > 0: # 스택에존재하고, 가장 최근에들어온 것이 num보다 작고, K지울것이 남아잇을때
            k -= 1
            stack.pop() #더 작으면 지워버림, 내가 생각했던 제거를 스택을 이용했음
        stack.append(num)
    if k != 0: # 지울게 남아있다면,
        stack = stack[:-k] # 스택의 뒷부분을 지워버림
    return ''.join(stack) # ''을붙임

#4321, 2 일때, while문을 들어가지 않고 4,3,2,1이 남고, 43을 출력하게 됨
#1234라면, while문에 들어가 1제거, 2제거 34가 남음
# 4177252841 , 4 라면, 4,1,7일때 while문에 들어가서 4,1제거, k-2되고 77252841이 되고, 25처럼 작은게들어가고 큰게들어가면 큰게 살아남게됨

# 잘못생각했던것은, 젤 작은것들만 제거하는게 아니고 높은 자리수 부터 비교해서, 큰수를 계속 살아남게 했어야했다.

#Stack등의 개념등을 항상 먼저 생각을 하고 아키텍쳐를 생각하고 코드를 시작해야겟다.

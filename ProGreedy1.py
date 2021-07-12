# 프로그래머스 코딩테스트연습 그리디알고리즘 체육복문제
# 너무 노가다로 푼 것 같다.
def solution(n, lost, reserve):
    answer = 0
    List1 = [1]*n
    count = n
    for i in range(len(lost)):
        List1[int(lost[i])-1] -= 1
    for j in range(len(reserve)):
        List1[int(reserve[j])-1] += 1
    for k in range(n):
        if List1[k] == 1:
            continue
        elif List1[k] == 0:
            if k > 0 and k+1 < n:
                if List1[k-1] == 2:
                    List1[k-1] = 1
                    continue
                elif List1[k+1] == 2:
                    List1[k+1] = 1
                    continue
                else:
                    count -= 1
            elif k == 0:
                if List1[k+1] == 2:
                    List1[k+1] = 1
                    continue
                else:
                    count -= 1
            elif n-1 == k:
                if List1[k-1] == 2:
                    List1[k-1] = 1
                    continue
                else:
                    count -= 1
        elif List1[k] == 2:
            continue

    answer = count
    return answer

# 다른 풀이. 접근방법과 시간복잡도는 동일하지만, 알아보기 쉽도록 간결하게 작성해보자.

def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1

        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer
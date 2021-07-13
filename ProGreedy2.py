# 프로그래머스 그리디알고리즘 조이스틱문제.
# 처음에 문제를 잘못이해해서 잘못 풀었다.
# enumerate함수와 ord활용법에 대해 알고가자.

def solution(name):
    answer = 0
    Joy =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #경우가 3개가 있음, 바로이동, 왼쪽에서부터이동, 오른쪽에서부터이동 3가지경우중에 작은것 선택
    #총 인덱스 0~25, 왼쪽시작은 (인덱스+1), 오른쪽은 26 - Joy.index('?'), 바로이동은 index(x)-현재
    A = Joy.index(name[0])
    answer += A
    print(A)
    for i in range(1, len(name)):
        leftstart = Joy.index(name[i])+1  # A는 시작 인덱스값
        rightstart = 26-Joy.index(name[i])
        Gostart = abs(Joy.index(name[i]) - A)
        A = min(leftstart, rightstart, Gostart)
        print("?",A)
        answer += A
        A = Joy.index(name[i])
        print(A)
    return answer

name="JEROEN"
solution(name)

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer

name = "JEADFfFSADDFSASDFAVLDSMV"
solution(name)

# enumerate는 index와 값의 튜플로 만들어줌
# 따라서 i가 인덱스, char이 값이됨
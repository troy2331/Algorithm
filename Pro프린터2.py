
# 프로그래머스 스택/큐 레벨2 < 프린터 >
# 프린터는 인쇄 요청이 들어온 순서대로 인쇄, 하지만 보완하기위해 중요도가 높은 문서를
# 먼저 인쇄하는 프린터를 개발함.
# 인쇄대기목록 가장 앞 문서 꺼냄 -> 이거보다 중요도가 높은것이 하나라도 존재하면 J를 맨 뒤로
# 아닐경우 인쇄
# 9151
from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    count = len(priorities)-1
    while location != -999:
        if priorities[0] != max(priorities): #첫번째께 젤 큰게 아닐때
            a = priorities.popleft()
            priorities.append(a)
            location -= 1
            if location == -1 :
                location = len(priorities)-1
        elif priorities[0] == max(priorities): # 첫번째께 젤 클때
            b = priorities.popleft()
            location -= 1
            answer += 1
            if location == -1:
                location = -999
                break
    return answer
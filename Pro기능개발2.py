# 프로그래머스 레벨2단계 문제 기능개발

from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    count = 1
    coun = 0
    while progresses:
        a = progresses[0] + count*speeds[0]
        if a >= 100:
            coun += 1
            progresses.popleft()
            speeds.popleft()
        elif a < 100:
            count += 1
            if coun > 0:
                answer.append(coun)
                coun = 0
    answer.append(coun)
    return answer
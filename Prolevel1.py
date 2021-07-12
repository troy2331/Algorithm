# 프로그래머스 -> 해시 -> 완주하지 못한 선수
# 내 풀이

def solution(participant, completion):
    # answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] == participant[-1]:
            answer = participant[i]
            return answer
            break
        elif participant[i] == completion[i]:
            continue
        elif participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

# 다른사람 풀이

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
# 데이터 개수를 셀 때 dictionary를 많이 사용하는데
# 파이썬에서 collections.counter를 이용할수도 있다.
from collections import Counter

Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 애초에 해시 문제이기 때문에, 해시함수를 이용한 풀이가 좋은 풀이라고 생각함
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

딕셔너리를 정의하고, hash()메소드를 이용하여 각각의 데이터에 대한 고유의 해시값을 저장한다.
그리고 모든 해시값을 더하고, completion에서 해시값을 뺴면, 차이가 생기는 그 값이
바로 완주하지 못한 해시값이 된다. 

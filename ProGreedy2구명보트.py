'''
문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.'''

#프로그래머스 구명보트
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    now = 0
    a = []
    for i in range(len(people)):
        if limit - people[0] < people[-1]: #한개로만타야되는것 빼기
            answer += 1
            people.pop(0)
        else:
            break
    m=0
    count=0
    while people: # people존재하면
        if now+people[-1] > limit:
            answer += 1
            now = 0
            m=0
            count =0
        elif now+people[m] <= limit:
            count += 1
            now = now+people[m]
            people.pop(m)
            if count == 2:
                now += 240
            if not people:
                answer+=1
        else:
            m += 1
    return answer

#정확성케이스 모두 맞았는데, 효율성에서 틀렸다.


def solution(people, limit):
    answer = 0
    people.sort() # [9,8,7,6,5,4,3,2,1]
    now = 0
    a = []
    for i in range(len(people)):
        if limit - people[-1] < people[0]: #한개로만타야되는것 빼기
            answer += 1
            people.pop()
        else:
            break
    m=0
    count=0
    people.sort(reverse = True)
    while people: # people존재하면
        if now+people[-1] > limit:
            answer += 1
            now = 0
            m=0
            count =0
        elif now+people[m] <= limit:
            count += 1
            now = now+people[m]
            people.pop(m)
            if count == 2:
                now += 240
            if not people:
                answer+=1
        else:
            m += 1
    return answer

# pop(m)은 시간복잡도 O(N)이고, pop()은 O(1)이라고 한다.
# 답안을 확인해봤을때, 최소, 최대를 짝 지었다.
# 나는 반례가 있을거라고 생각해서 최대+ (최소중에 가장 큰 것)을 뽑느라 시간복잡도가 매우 높아졌다.
# x y z w , xw yz 이렇게 안되는 경우의수가 있을까? xz, yw
# x>y>z>w , limit > xw, yz / xz, yw 오른쪽상황이 되는데 왼쪽이 안되는 경우의수가 있다면
# 내생각이 맞는것인데
# 95 90 5 1 / 없다. 먼저 미지수조건으로 잘 판단하여 코드에 들어가도록 주의하자


def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people)-1
    while i <= j:
        cnt += 1
        if people[j]+people[i] <= limit:
             i += 1
        j -= 1
    return cnt
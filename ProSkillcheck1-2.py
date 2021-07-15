def solution(seoul):
    i=0
    t=0

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            t = i
            break
    answer = "김서방은 {}에 있다".format(t)

    return answer
def solution(n):
    answer = 0
    i = 0
    n = str(n)
    for i in range(len(n)):
      answer += int(n[i])
      i += 1

    return answer
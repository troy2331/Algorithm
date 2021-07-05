#서로 다른 N개의 자연수의 합이 S, S를 알 때 자연수 N의 최댓값?
import sys
input = sys.stdin.readline
N = int(input())
i = 1
count = 0
if N == 1:
    print(1)
elif N==0:
    print(0)
else:
    while 0 <= N:
      if N < 0:
          count -= 1
          break
      N -= i
      count += 1
      i += 1
    print(count-1)


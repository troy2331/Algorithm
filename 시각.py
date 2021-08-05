# 시각, 정수N이 입력되면 00시00분00초부터 N시 59분 59초까지의 시각중에 3이 하나라도 포함되는 경우의수를 구하는 프로그램
# 완전탐색유형, 모든경우의수를 세어도 10만개가 넘어가지 않음

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
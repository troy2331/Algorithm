# 백준 10162번 전자레인지
# 3개의 시간조절용 ABC 각각 5분, 1분, 10초
N = int(input())
A = 0
B = 0
list1 = [300, 60, 10]
list2 = [0,0,0]
for i in range(3):
    list2[i] = N//list1[i]
    N = N%list1[i]
if N != 0 :
    print(-1)
else:
    print(list2[0],list2[1],list2[2])
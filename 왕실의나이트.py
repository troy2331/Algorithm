# 왕실정원은 8*8 좌표평면에서, 나이트는 수평두칸,수직한칸 or 수직2칸,수평한칸 이동 가능
now = input()
row = int(now[1])
column = int(ord(now[0]))-int(ord('a'))+1 # 입력값이 ex)a1 이기 때문에, 유니코드값으로 바꿔줌

step = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2),(-2,1)]

result = 0
for i in step:
    next_row = row+i[0]
    next_column = column + i[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result+=1
print(result)
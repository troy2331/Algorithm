# 백준 1339 단어 수학
# 단어 수학은 N개의 단어로 이루어져 있고, 0~9숫자중 하나로 바꾸어 N개의수로 합하는 문제
# 최대가 되게끔 하는 프로그램
# 입력 2, AAA, AAA 이면 1998출력
# 제일 긴 단어를 9부터 할당, 같은자릿수라면 차례차례 내림차순 할당, 동일한숫자는 패스
# 중요도, ABC라면, A:100, B:10, C:1 로 중요도를 총 더한 후 9부터 할당.
# 딕셔너리를 이용

n = int(input())
words = []
for i in range(n):
    words.append(input())
dict = {}
for word in words:
    k=len(word)-1
    for s in word:
        if s in dict:
            dict[s] += pow(10,k)
        else:
            dict[s] = pow(10,k)
        k-=1
nums=[]
for value in dict.values():
    nums.append(value)

nums.sort(reverse=True)
result, t = 0,9
for i in range((len(nums))):
    result += nums[i]*t
    t-=1
print(result)
import sys

input = sys.stdin.readline

str1 = ' ' + input().rstrip()
str2 = ' ' + input().rstrip()

dp = [[""] * len(str2) for _ in range(len(str1))]


for i in range(1,len(str1)):
    for j in range(1,len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + str1[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

result = dp[-1][-1]  # 인덱스를 한번만 참조하게 REsult 변수에 미리 담아놔야 시간초과 안뜸
print(len(result))
print(result)


'''
    [효율성]
    -메모리 : 55712 KB
    -시간 : 540 ms
'''
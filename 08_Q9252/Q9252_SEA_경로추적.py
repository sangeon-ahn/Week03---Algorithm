# 경로 추적 방법은 문자열 저장 방법과 달리 문자열을 계속 저장할 필요가 없고 dp 배열로만 lcs를 구할 수 있다.
s1 = input()
s2 = input()
dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[j + 1][i + 1] = dp[j][i] + 1
        else:
            dp[j + 1][i + 1] = max(dp[j][i + 1], dp[j + 1][i])

y = len(s1)
x = len(s2)
ans = ""

while 1 <= x and 1 <= y:
    if dp[x][y] == dp[x - 1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y - 1]:
        y -= 1
    else:
        ans += s2[x - 1]
        x -= 1
        y -= 1

print(dp[len(s2)][len(s1)])
if dp[len(s2)][len(s1)] != 0:
    print(ans[::-1])

"""
493832	928
"""
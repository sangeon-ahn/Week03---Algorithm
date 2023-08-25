N = int(input())
dp = [0] * (N + 10) # dp[i]: i 크기의 공간에 타일을 배치할 수 있는 가지수
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])

"""
    메모리: 122133
    시간: 136ms
"""
N, M = map(int, input().split())
smalls = set([int(input()) for _ in range(M)])
"""
우선, 2차원 dp 배열을 사용하고, dp[i][j]: i번째 돌을 스피드 j로 도달했을 경우에 칸 움직인 횟수
dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
우선 다 sys.maxsize로 초기화, dp[1][0] = 0, dp[2][1] = 1
"""
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)]
dp[1][0] = 0

for i in range(2, N + 1):
    if i in smalls:
        continue

    for spd in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][spd] = min(dp[i - spd][spd - 1], dp[i - spd][spd], dp[i - spd][spd + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))
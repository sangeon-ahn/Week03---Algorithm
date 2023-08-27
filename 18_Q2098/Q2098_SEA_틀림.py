"""
A, B, C, D, E 도시가 있다.
A에서 출발했다.
도시 B로 갔다고 치자.
도시 B로 오기 전에 어디에 있었을까?

우선, dp 테이블에 weights를 다 채워넣음.
이후, dp[i][j] = dp[i][x] + W[x][j]를 세워서
3중 for문 돌려서 dp를 다 채운다.

"""

N = int(input())
Weight = [list(map(int, input().split())) for _ in range(N)]
dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if Weight[i][j] == 0:
            dp[i + 1][j + 1] = float('inf')
        else:
            dp[i + 1][j + 1] = Weight[i][j]

# dp[i][j]: (i, j)로 가는 가장 최단거리, 이후 dp[i][i]중 가장 작은걸 뽑으면 됨

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue

        for k in range(1, N + 1):
            if k == i or k == j:
                continue

        
            dp[i][k] = dp[i][j] + Weight[j - 1][k - 1]
        
check = [True] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if Weight[j - 1][i - 1] != 0:
            dp[i][j] += Weight[j - 1][i - 1]
        else:
            check[]

# for i in range(len(dp)):
#     print(dp[i])


ans = float('inf')
for i in range(len(dp)):
    ans = min(ans, min(dp[i]))

print(ans)

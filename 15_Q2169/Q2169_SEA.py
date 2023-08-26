import sys
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

"""
dp[i][j]: (i, j) 에 위치해 있을 때 최대 가치합
왼쪽, 오른쪽으로 갈 수 있기 때문에 왼쪽으로만 갈 경우, 오른쪽으로만 갈 경우 두개로 나눠서 얻을 결과 중 더 큰값을 취한다.
이때, 임시 배열 2개를 만들어서 이 값에 임시 dp결과값을 저장하고, 같은 행에 대해 임시테이블2개를 다 채웠으면 두 값을 비교해서 더 큰값을 진짜 dp테이블에 넣는다. 
"""
dp = [[-sys.maxsize] * (M + 2) for _ in range(N + 2)]
temp_table1 = [-sys.maxsize] * (M + 2)
temp_table2 = [-sys.maxsize] * (M + 2)
dp[1][0] = 0
for i in range(M):
    dp[1][i + 1] = dp[1][i] + board[0][i]

for i in range(2, N + 1):
    for j in range(1, M + 1):
        if temp_table1[j - 1] > dp[i - 1][j]:
            temp_table1[j] = temp_table1[j - 1] + board[i - 1][j - 1]
        else:
            temp_table1[j] = dp[i - 1][j] + board[i - 1][j - 1]
    
    for j in range(1, M + 1):
        if temp_table2[M + 2 - j] > dp[i - 1][M + 1 - j]:
            temp_table2[M + 1 - j] = temp_table2[M + 2 - j] + board[i - 1][M - j]
        else:
            temp_table2[M + 1 - j] = dp[i - 1][M + 1 - j] + board[i - 1][M - j]

    for j in range(1, M + 1):
        if temp_table1[j] > temp_table2[j]:
            dp[i][j] = temp_table1[j]
        else:
            dp[i][j] = temp_table2[j]    

print(dp[N][M])




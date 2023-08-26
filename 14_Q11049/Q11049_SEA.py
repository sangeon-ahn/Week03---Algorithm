import sys
N = int(input())
"""
5 3
3 2
2 6
(5 * 3 * 2) + (5 * 2 * 6)
3 * 2 * 6 + 5 * 3 * 6
"""

# 우선, (2X2) 행렬의 연산 횟수는 r1*c1*c2이기 때문에 (r,c)행렬 데이터를 받을 때, ㄱ자 모양으로 받아서 저장하고 사용하는기법
abstracted_mats = list(map(int, input().split()))
for i in range(N - 1):
    r, c = map(int, input().split())
    
    # 열 데이터만 넣는다.
    abstracted_mats.append(c)

# 이제 dp 테이블을 구성한다.
# dp[i][j]: i번째 ~ j번째 행렬을 다 곱해서 하나의 2차원 행렬을 만들었을 때, 가장 작은 연산횟수 = dp[i][j]
# 예1: dp[0][0]: 0번째 ~ 0번째 이므로 행렬 하나만 있어서 연산횟수 0
# 예2: dp[0][1]: 0번째 ~ 1번째 이므로 그냥 두 행렬 곱해주면 되고 abstract[0] * abstract[1] * abstract[2]

# 최솟값 구해야해서 다 맥스로 초기화
dp = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]
# 범위 크기가 1일때는 필요연산 0개
for i in range(N):
    dp[i][i] = 0

# dp테이블 채우기

# 0 <= length <= N - 1
# 길이 0일 때 쫙 돌고,
for length in range(1, N):
    # 언제까지 돌아? start가 N - length 될때까지
    # 왜? length = 0일 때 보면 start == end == N-1 까지 되고 이때 dp테이블에서 맨 밑 맨 오른쪽 부분이라 그렇다.
    # 아래는 dp테이블에서 얼마나 밑에까지 갈지를 결정하는 for문이다.
    for start in range(N - length):
        end = start + length
        
        # dp[start][end]를 구하면 된다.
        
        # 범위에 행렬이 2개뿐이면 그냥 곱해주면 된다.
        if end - start == 1:
            dp[start][end] = abstracted_mats[start] * abstracted_mats[start + 1] * abstracted_mats[end + 1]
        
        # 범위에 행렬이 3개 이상이면 for문 돌려야 한다.
        else:
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + abstracted_mats[start] * abstracted_mats[mid + 1] * abstracted_mats[end + 1])

"""
왜 2차원 dp 테이블의 (왼쪽 위, 오른쪽 아래를 연결해서 만든 대각선)을 위로 1만큼 평행이동해서 만든 대각선 순서로 채워주어야 하는가?
-> dp[0][8] 결과를 확정짓기 위해서는 (dp[0][0], dp[1][8]), (dp[0][1], dp[2][8]), (dp[0][2], dp[3][8]) ..., (dp[0][7], dp[8][8]) 이런식으로 dp[8][8]을 기준으로 가로선에 속하는 dp값과 세로선에 속하는 dp값을 모두 알고 있어야 한다. 이렇게 해서 가장 먼저 알고 있어야 하는 지점들을 파고 내려가다 보면 (왼쪽 위, 오른쪽 아래를 연결해서 만든 대각선) 으로 까지 오게 된다. 따라서 저 순서대로 채워주어야 우리가 원하는 값이 있는 dp[0][N - 1]값을 올바르게 구할 수 있다.
"""

print(dp[0][N - 1])


        


    


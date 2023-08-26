import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
smalls = set([int(input()) for _ in range(M)])

dp = [-1] * (N + 1) # dp[i]: i번째 돌 가는데 걸리는 횟수 
dp[1] = 0

def recur(speed, pos, cnts): # 속도, 위치, 횟수
    global N, dp
    if pos > N:
        return
    
    if pos == N:
        return

    for x in [speed - 1, speed, speed + 1]:
        # 이동을 안하거나 밖으로 가면 패스
        if pos + x < 1 or pos + x > N or x < 1:
            continue

        # 가지 말아야 할 돌이면 패스
        if pos + x in smalls:
            continue

        # 아직 해당 위치에 도달한 적이 없으면 가기
        if dp[pos + x] == -1:
            dp[pos + x] = cnts + 1 
            recur(x, pos + x, cnts + 1)
        
        # 도달한 적이 있는데 더 빠른 경로를 찾았으면 가기
        elif cnts + 1 < dp[pos + x]:
            dp[pos + x] = cnts + 1
            recur(x, pos + x, cnts + 1)
        
        # 도달했는데 이미 더 빨리 가는 법이 있으면 패스
    
recur(1, 2, 1)

print(dp[N])




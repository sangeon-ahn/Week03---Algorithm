N = int(input())
Weight = [list(map(int, input().split())) for _ in range(N)]

# 열 개수를 외판원 경로의 경우의 수만큼으로 해줌으로써 모든 경로 체크 가능하도록 함. 비트연산을 위해서.
# dp[init_node][visited]: 출발 노드 init_node에서 시작해서 현재 방문한 도시들 정보는 visited에 있고, 아직 방문하지 않은 도시들을 다 방문하는데 드는 비용 + 다 방문했을 때 다시 시작도시로 돌아가는 비용 
# 예: N = 5일 때, dp[1][7]: 시작도시 = 1, 방문한 도시들 정보: 7_(10) = 111_(2)라서 0, 1, 2 도시 방문 완, 3, 4 도시 아직 미방문. 따라서 dp[1][7] = 현재 도시 -> (3, 4) 도시를 방문하고 다시 1로 돌아오는데 드는 최소 비용. 
dp = [[-1] * (1 << N) for _ in range(N)]

# (현재 노드, 지금까지 방문한 도시들)
# 리턴값은 cur에서 visited도시들 방문한 상태일 때 다시 나머지 도시 다 돌고 cur로 오는 최소비용
def recur(cur, visited):
    # 모든 노드를 방문했으면,
    # 예: N = 5면 1 << 5 = 100000이고, 1 << 5 - 1 = 11111이다.
    # visited == 11111이면 5자리 전부 1이므로 모든 도시를 한번씩 방문한 상태다.
    if visited == (1 << N) - 1:
        # cur도시에서 0으로 가는 경로가 없으면 무한대 리턴
        if Weight[cur][0] == 0:
            return float('inf')
        
        # 있으면 
        dp[cur][visited] = Weight[cur][0]
        return Weight[cur][0]
    
    # 아직 다 방문 안했을 때,

    # dp에 저장한거 있으면 쓰기
    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    # 없으면 새로 만들기
    min_dist = float('inf')
    
    # 현재 도시(cur)에서 visited만큼 방문했을 때, 나머지 도시를 방문하고 다시 0도시로 오는 최소비용을 구하는 for문
    for i in range(N):
        # 아직 i번째 노드는 방문 안했고 weight가 0이 아니면 갈 수 있음.
        if not visited & (1 << i) and Weight[cur][i] != 0:
            rest = recur(i, visited | (1 << i))
            min_dist = min(min_dist, Weight[cur][i] + rest)
    
    # 위에서 구한걸 dp에 넣고 리턴.
    dp[cur][visited] = min_dist
    return min_dist

print(recur(0, 1))


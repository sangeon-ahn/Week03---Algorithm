import sys
N = int(input())
Weights =[list(map(int, input().split())) for _ in range(N)]
"""
dp[start][visited]: 시작 노드 start에서 현재까지 visited에 속하는 도시들을 방문한 상태일 때, 여기서부터 비용 집계를 시작하여 나머지 도시들을 전부 방문하고 다시 start로 오는데 필요한 비용합 
"""
dp = [[-1] * (1 << N) for _ in range(N)]

# (현재도시, 방문한 도시)
def recur(cur, visited):
    # 다 방문했을 때,
    if visited == (1 << N) - 1:
        # 시작도시로 갈 수 있다면,
        if Weights[cur][0] != 0:
            # dp에 저장하고,
            dp[cur][visited] = Weights[cur][0]
            # 리턴한다.
            return Weights[cur][0]
        # 갈 수 없다면?
        else:
            # 맥스값을 리턴해서 해당 경로는 사용되지 않도록 한다.
            return sys.maxsize
    
    # dp에 있으면 그거 쓰기
    if dp[cur][visited] != -1:
        return dp[cur][visited]

    # 아직 방문 못한 경우 방문하러 간다.
    min_dist = sys.maxsize

    # 다음으로 갈 도시 순회
    for nxt_city in range(N):

        # 방문 안했고 갈 수 있으면 가기
        if not visited & (1 << nxt_city) and Weights[cur][nxt_city] != 0:
            min_dist = min(min_dist, Weights[cur][nxt_city] + recur(nxt_city, visited | (1 << nxt_city)))
    
    dp[cur][visited] = min_dist
    return min_dist

print(recur(0, 1))

        

        

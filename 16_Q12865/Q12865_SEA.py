N, K = map(int, input().split())
items = [[0, 0]]
bag = [[0] * (K + 1) for _ in range(N + 1)]
"""
물건을 하나씩 순회하면서, 해당 물건을 넣을 수 없으면 다음으로 가고, 넣을 수 있으면(무게 < K), dp[K - 무게]값과 현재 dp[K]값을 비교해서 더 큰값을 넣는다.??
"""

for _ in range(N):
    items.append(list(map(int, input().split())))

# 1번째 아이템부터 N번째 아이템까지 순회
for i in range(1, N + 1):
    # 목표무게를 1부터 K까지 올리면서 dp (bag) 채우기
    for weight_goal in range(1, K + 1):
        weight, value = items[i]

        # 목표 무게보다 현재 아이템의 무게가 더 크면 못넣으니까 이전 아이템 차례였고, 같은 목표무게였을 때의 총 가치합을 넣기
        if weight_goal < weight:
            bag[i][weight_goal] = bag[i - 1][weight_goal]
        
        # 목표 무게가 더 크면 (해당 아이템을 챙겼을 경우, 챙기지 않았을 경우) 중 더 총 가치합이 큰 경우를 택한다.
        # 챙긴 경우라면, 목표 무게에서 해당 아이템을 뺀 무게만큼으로 가장 가치가 높게 담을 수 있는 경우 + 해당아이템의 가치
        # 안 챙긴 경우라면, 해당 아이템을 보기 전까지의 가장 높은 가치
        # 가장 높은 가치는, 이전 아이템까지 다 보았고, 가방의 목표 무게가 가장 클 때 가장 높다.
        else:
            bag[i][weight_goal] = max(bag[i - 1][weight_goal - weight] + value, bag[i - 1][weight_goal])

print(bag[N][K])



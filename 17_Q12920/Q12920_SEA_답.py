N, M = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (M + 1)
# 1, 2, 4, 8 이런식으로 묶어서 weights, satis 배열에 넣는다.
# weights를 돌면서 내부에서 넣을 수 있는 무게를 돌면서 넣을 수 있으면 넣는다.
# 다 돌았으면 dp[N]을 출력한다.
weights = []
stis = []

for item in items:
    v, c, k = item
    
    temp = 1
    while k > 0:
        mul = min(temp, k)

        weights.append(v * mul)
        stis.append(c * mul)
        
        temp *= 2
        k -= mul


# 무게 돌면서
for i in range(len(weights)):
    # 목표무게는 M부터 낮춰주면서 dp 채우기
    for weight_goal in range(M, 0, -1):
        if weight_goal >= weights[i]:
            dp[weight_goal] = max(dp[weight_goal], dp[weight_goal - weights[i]] + stis[i])

print(dp[M])
        
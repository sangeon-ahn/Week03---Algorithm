"""
이전 문제와의 차이점은, 동전의 주어진 개수가 제한이 없다는 거다.
그래서 cnts를 순회하는게 아니라 money를 초과하기 전까지 순회하면 된다.
"""

T = int(input())

for _ in range(T):
    N = int(input())
    values = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in values:
        for money in range(target, 0, -1):
            cnt = 1

            while money - coin * cnt >= 0:
                dp[money] += dp[money - coin * cnt]
                cnt += 1
    
    print(dp[target])


"""
114488kb	140ms
"""
        
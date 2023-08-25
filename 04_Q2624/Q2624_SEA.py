T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]
coins.sort(key=lambda coin: coin[0])

"""
    1원: 5개, 5원: 3개, 10원: 2개
    dp = [0] * (T+1) # dp[n] : n 금액에 대한 동전 교환 방법의 가지 수 
    1차원
    dp[i]: i원을 만드는 방법 개수
    dp[1]: 1
    dp[2]: 1
    dp[3]: 1
    dp[4]: 1
    dp[5]: 2
    dp[6]: 1
    dp[7]: 1
    dp[8]: 1
    dp[9]: 1
    dp[10]: 3
    dp[11]: 2
"""
dp = [0] * (T + 1)
dp[0] = 1

for coin in coins:
    value, cnts = coin # (가치, 개수)

    # 끝에서부터 1까지 순회하면서 money - value * i를 만들 수 있는 개수를 money를 만들 수 있는 개수에 추가시켜준다.
    # 왜 끝에서? -> 앞에서부터 하면 이전에 더했던게 중복해서 더해져서 누적이 돼버림
    # 끝에서부터 하면 왜 이 현상이 없는지?
    # 앞에서부터 하면, dp[2] += dp[2 - 1], dp[2] += dp[2 - 2] 이렇게 두번 더해지는데, dp[1] = 1이고, dp[0] = 1이라서 dp[2] = 2가 된다. 하지만 0원에서 1원 2개를 더하나, 1원에서 1원 1개를 더하나 모두 같은 경우였기 때문에 오류다.
    # 따라서, coin = (1, 5)이고 money = 2일 때, dp[2] = dp[2 - 1*1 = 1] = 0이고, dp[2] = dp[2 - 1*2 = 0] = 1이라서 dp[2]] = 1이다. 이때는 자기 코인을 사용하지 않고 만든 경우의 수만 사용해서 더해주는 셈이 된다.
    for money in range(T, 0, -1):
        for i in range(1, cnts + 1):
            if money - value * i >= 0:
                dp[money] += dp[money - value * i]

print(dp[T])


"""
    메모리        시간
	115272kb    224ms
"""


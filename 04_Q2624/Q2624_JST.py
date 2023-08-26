import sys
input = sys.stdin.readline

t = int(input()) # 지폐의 금액
k = int(input()) # 동전의 가지 수 
coins = [] # 동전 정보
dp = [0] * (t+1) # dp[n] : n 금액에 대한 동전 교환 방법의 가지 수 (경우의 수)
dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1로 초기화 => 앞의 경우의 수를 안 떙겨오고, coin만으로 금액 채울 때 사용

for _ in range(k):
    p, n = map(int, input().split())
    coins.append((p, n))

for coin, cnt in coins:
    for money in range(t, 0, -1): # t원부터 1원까지 내려가며 진행 
        for i in range(1, cnt+1): # 현재 동전 coin의 개수만큼 for문 진행 
            if money - coin * i >= 0: # coin을 i개 썼을 때 구하려고 하는 금액보다 크지 않으면.
                dp[money] += dp[money - coin * i] #코인 i개를 사용했을 때 남은 금액에 대한 경우의 수를 DP에서 찾아 합함
                                                    #ex)coin이 10 이며 1개만 썼을 때 남은 금액은 10이다.
                                                    # dp에 다른 Coin으로 10원을 만든 경우의 수가 있다면 그걸 합한다.
                                                    #그것이 10원 동전 하나를 사용했을 떄의 경우의 수.


print(dp[t])


'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 4828 ms
'''



# from functools import lru_cache

# @lru_cache(maxsize=None)
# def count_coin_combinations_recursive(target_money, coin_index):
#     if target_money == 0:
#         return 1
    
#     if target_money < 0 or coin_index < 0:
#         return 0
    
#     coin, cnt = coins[coin_index]
#     combinations = 0
    
#     for i in range(cnt + 1):
#         combinations += count_coin_combinations_recursive(target_money - coin * i, coin_index - 1)
    
#     return combinations

# import sys
# input = sys.stdin.readline

# t = int(input())
# k = int(input())
# coins = []

# for _ in range(k):
#     p, n = map(int, input().split())
#     coins.append((p, n))

# result = count_coin_combinations_recursive(t, k - 1)
# print(result)
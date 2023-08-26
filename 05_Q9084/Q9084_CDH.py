import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M+1)
    dp[0] =1
    # count 가 없어!!
    
    # maxCount = 1
    # for coin, idx in enumerate(coins):
    #         while(True):
    #             if(coin * maxCount < M):
    #                 maxCount+=1;
    #             else:
    #                 coins[idx].append(maxCount)
    #                 break;
                
    # print(coins)
    for coin in coins: # 순서
        for money in range(M, 0, -1):
         # 1,2
            for i in range(1, 10001):
                if(money >= (i * coin)):
                    dp[money] += dp[money - (i*coin)]
    print('dp',dp)  
    print(dp[M])
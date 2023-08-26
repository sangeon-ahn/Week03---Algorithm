import sys

tcase = int(sys.stdin.readline())

for _ in range(tcase):
    n = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    m = int(sys.stdin.readline())
    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1,m+1):
            if coin <= i:
                dp[i] += dp[i-coin]

    print(dp[m])


    '''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 76 ms
'''
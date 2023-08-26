import sys
from sys import maxsize

n,k = map(int,sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i],dp[i-coin]+1) #현재 값에서 가져온 코인 값을 빼주었을 때의 코인 사용 개수(남은 금액)에 지금 코인 개수 하나를 더한 값

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])


'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 396 ms
'''
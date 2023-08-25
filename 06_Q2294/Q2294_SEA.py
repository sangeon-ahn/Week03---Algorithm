import sys
n, k = map(int, input().split())
values = list(set([int(input()) for _ in range(n)]))

"""
동전의 합이 k가 되도록 하는 문제
이전, 그 이전 문제는 합이 k가 되는 경우의 수가 몇 개 인지를 구하는 문제였다.
지금 문제는, 합이 k가 되는 경우의 수 중 가장 동전을 적게 쓰는 경우를 구하는 문제다.
그래서 더해줄 때, dp[i] = min(dp[i], dp[i-x] + 1) 이렇게 해서 min(기존 i 만드는데 필요한 개수, i-x에 x 만큼 더해서 구할 때 필요한 개수 + x 1개 더해주기) 해주면 된다.
dp[5] = min(dp[5], dp[5 -5] + 1)에서 기존 dp[5] = 5였고, dp[0] + 1 = 1이라서 dp[5] = 1로 갱신
dp[10] = min(dp[10], dp[10 - 5] + 1)에서 dp[10] = 10, dp[5] + 1 = 2라서 2로 갱신
dp[15] = min(dp[15], dp[15 - 5] + 1)에서 dp[15] = 15, dp[10] + 1 = 3이라서 3으로 갱신
따라서 이전 문제 때 사용했었던 cnts변수를 사용하지 않고도 누적이 된다.
3 15
1
5
12
"""
dp = [sys.maxsize] * (k + 1)
dp[0] = 0

for value in values:
    for money in range(value, k + 1):
        dp[money] = min(dp[money], dp[money - value] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])



"""
115284kb	136ms
"""


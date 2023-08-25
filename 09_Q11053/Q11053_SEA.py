N = int(input())
nums = list(map(int, input().split()))

"""
dp[i]: i번째 수를 최장 부분수열의 가장 큰 값으로 가질 때 해당 부분수열의 길이
dp[i]: k < i일 때, nums[i] > nums[k] 이면 dp[i] = max(dp[i], dp[k] + 1)
"""

dp = [1] * (N + 1)

for i in range(2, N + 1): # 2부터 N까지 돌기
    for j in range(1, i): # 1부터 i - 1까지 돌기
        # i번째 값보다 j번째가 작으면 갱신
        if nums[i - 1] > nums[j - 1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp[N]))

"""
114488kb	140ms
"""
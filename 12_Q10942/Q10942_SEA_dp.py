import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
questions = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(n)]

# 길이 0부터 n - 1 까지
for num_len in range(n):
    # 시작 인덱스: 0부터 n - num_len - 1 까지
    for start in range(n - num_len):
        end = start + num_len # 5 - 0 = 5, 0 + 0 = 0
        
        if start == end:
            dp[start][end] = 1
        
        elif numbers[start] == numbers[end]:
            if end - start == 1:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for q in questions:
    print(dp[q[0] - 1][q[1] - 1])

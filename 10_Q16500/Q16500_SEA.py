S = input()
N = int(input())
A = [input() for _ in range(N)]

"""
dp[i]: S의 i번째부터 끝까지 부분문자열을 주어진 단어로 만들 수 있으면 1, 없으면 0
"""

dp = [0] * (len(S) + 1) 
# 끝dp = 1
dp[len(S)] = 1

for i in range(len(S) - 1, -1, -1):
    # i는 마지막 문자부터 시작해서 첫번째 문자까지 가면서 i 이후의 문자열을 만들 수 있나 없나 확인
    for word in A:
        # 일단 해당 구간이 단어랑 같고(S[i:i + len(word)]),
        # 그 이후는 모두 만들 수 있어야 함(dp[i + len(word)] == 1).
        if  S[i:i + len(word)] == word and dp[i + len(word)] == 1:
            dp[i] = 1
            break

print(dp[0])

"""
114488kb	144ms
"""


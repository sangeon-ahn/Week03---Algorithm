S = input()
dp = [[False] * (len(S) + 1) for _ in range(len(S) + 1)]
dp2 = [2500] * (len(S) + 1)
dp2[-1] = 0
for length in range(len(S)):
    for start in range(len(S) - length):
        end = start + length

        # 일단 같은지 본다.
        if start == end:
            dp[start][end] = True
            continue
        
        # 안 같은 경우.
        
        # 시작, 끝이 같으면,
        if S[start] == S[end]:
            if end - start == 1:
                dp[start][end] = True
            elif dp[start + 1][end - 1]:
                dp[start][end] = True
                
for end in range(len(S)):
    for start in range(end + 1):
        if dp[start][end]:
            dp2[end] = min(dp2[end], dp2[start - 1] + 1)
        else:
            dp2[end] = min(dp2[end], dp2[end - 1] + 1)

print(dp2[len(S) - 1])
            


        
            



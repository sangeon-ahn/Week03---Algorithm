s1 = input()
s2 = input()
dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
saved = [[""] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            saved[j][i] = saved[j - 1][i - 1] + s1[i - 1]
        else:
            if len(saved[j][i - 1]) > len(saved[j - 1][i]):
                saved[j][i] = saved[j][i - 1]
            else:
                saved[j][i] = saved[j - 1][i]

# for i in range(len(dp)):
#     print(dp[i])

# for i in range(len(saved)):
#     print(saved[i])

lcs = saved[len(s2)][len(s1)]
print(len(lcs))

if len(lcs) != 0:
    print(lcs)

"""
122828	168
"""
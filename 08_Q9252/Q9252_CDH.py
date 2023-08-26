import sys
input = sys.stdin.readline

S1 = str(input().rstrip())
S2 = str(input().rstrip())

len1 = len(S1)
len2 = len(S2)

dp = [0] * (len1+1)
for i in range( len1):
    for j in range( len2):
        if(S1[i] == S2[j]) and i<=j:
            dp[i] = S1[i]

result = ''    
for i in dp:
    if(type(i) == int):
        continue;
    else:
        result +=i
print(len(result))
print(result)
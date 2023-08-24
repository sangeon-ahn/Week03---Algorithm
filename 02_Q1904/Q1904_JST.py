#Bottom Up방식

#이 문제는 탑다운(재귀)로 풀면 메모리 초과가 뜬다.

import sys

dp = [0]*1000001

dp[1] = 1
dp[2] = 2

n = int(sys.stdin.readline())

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    #나중에 print 할 때 나누면 메모리 부족이라 미리 나눠준다.

print(dp[n])

'''
    [효율성]
    -메모리 : 69788 KB
    -시간 : 344 ms
'''
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split(' ')))

dp = [1] * n #dp[i] = a[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

#참조
#https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC


'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 160 ms
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
money = list()
for _ in range(n):
    money.append(int(input()))

money.sort()

def rec(i,sum):
    coin = money[i]
    if coin > k:
        return
    coinsum = coin
    i = 1
    while coinsum < k:
        if coinsum == k:
            return
        i+=1
        coinsum = coinsum * i


rec(-1,0)
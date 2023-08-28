import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
money = list()
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

i = 0
count = 0
while True:
    coin = money[i]
    if coin > k: # 코인 금액이 k이상이면 이 동전은 패스
        i += 1
        continue
    coinsum = coin * (k // coin)
    count += k // coin
    if coinsum == k: # 정답을 찾음
        print(count)
        break
    i+=1
    k = k - coinsum


'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 40 ms
'''
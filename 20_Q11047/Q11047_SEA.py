N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)][::-1]
print(coins)
"""
그리디 문제다. 문제에서 각 코인의 개수는 무한대이고, 동전가치_i는 동전가치_i-1의 배수다.
따라서 큰 가치는 작은 가치 몇개를 합치면 만들 수 있다.
그래서 큰 가치부터 사용해 가면서 더이상 가치가 잔여필요량보다 커질 때 더 가치가 낮은 동전을 사용하면 된다.
그리고 잔여가치를 지금 있는 가치로 못 만들 수 있을지도 모르는데 이게 아닌 이유는 1의 가치도 주어지기 때문이다.
"""
cnts = 0
idx = 0
while K > 0:
    # 남은 돈보다 현재 idx의 동전의 가치가 더 크면 패스
    if K < coins[idx]:
        idx += 1
        continue

    # 그 외에는 사용할 수 있는만큼 최대로 사용한다.
    temp = K // coins[idx]
    K -= temp * coins[idx]

    # 사용 횟수에 추가
    cnts += temp

    # 사용하고 보니까 K가 0이 됐으면 끝
    if K == 0:
        print(cnts)
        break

    # 안됐으면 다시 while 돌기



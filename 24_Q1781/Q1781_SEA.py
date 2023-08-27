import heapq, sys

N = int(input())
# 문제는 2차원 배열로 받는다. problems[i]: 데드라인이 i인 문제들의 컵라면이 담긴다.
problems = [[] for _ in range(200001)]

for _ in range(N):
    dead, cups = map(int, input().split())
    # 데드라인이 dead인 문제들의 컵라면이 담긴다.
    problems[dead].append(cups)

# 최대힙을 만들어준다.
hq = []
ans = 0
# 데드라인이 최대 20만이라서 20만 -> 1 순서로 큐에 넣어준다.
for dead in range(200000, 0, -1):
    # 우선 해당 데드라인인 문제들을 다 넣어준다.
    for cups in problems[dead]:
        # 컵수, 데드라인. 컵수 1순위(큰거부터), 데드라인 2순위(작은거부터)
        heapq.heappush(hq, -cups)

    if len(hq) == 0:
        continue
    
    # 이후 지금까지 넣어놨던 문제들 중 가장 컵라면을 많이 주는 문제를 뽑아 푼다.
    # 이렇게 데드라인을 내림차순으로 돌면서 한 데드라인에 해당하는걸 넣고 그중 탑을 뽑고 그 이전 데드라인을 넣고 이런식으로 구현하면, 데드라인이 1, 2, 3, 4, 5인 문제들이 있다고 칠 때, 5는 5번, 4는 4번, 3은 3번, 2는 2번, 1은 1번 뽑힐 기회가 주어진다.
    # 따라서 굳이 시간변수를 만들어줄 필요 없이, 뽑힐 기회를 부여함으로써 데드라인을 구현했다. 
    ans += -heapq.heappop(hq)
    
print(ans)

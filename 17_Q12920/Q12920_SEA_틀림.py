N, M = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
items.sort()

"""
    이전 문제를 응용한다. 이전 문제와 다른 점은, 아이템의 개수가 있다는거다.
    그래서 1차 for문: 아이템, 2차 for문: 목표무게 해두고, 2차 for문 내에서, 해당 아이템이 x개 있으면 1개 넣을 경우부터 시작해서 x개 넣을 경우까지 확인해서 dp 테이블에 추가시켜준다. 물론 이때, 목표무게를 초과하지 않는 선까지만 가능하다.
"""

# 우선 dp 테이블 역할을 하는 가방을 만들어준다.
bag = [[0] * (M + 1) for _ in range(N + 1)]

# items를 순회 -> 목표 무게를 순회하며 bag 테이블을 채운다.
for i in range(len(items)):
    # 값을 추출한 후,
    weight, value, cnts = items[i]
    
    # 목표 무게를 1부터 M까지 해서 bag을 채운다.
    for weight_goal in range(1, M + 1):

        # 넣을 수 있는지 판단한 후 못 넣으면 이전 아이템꺼 최대값이랑 비교해서 넣는다.
        if weight_goal < weight:
            bag[i + 1][weight_goal] = bag[i][weight_goal]

        # 넣을 수 있으면 넣는데, 최대로 넣을 수 있는 만큼 넣는 것과, 이전 값 중 더 큰값을 취한다.
        else:
            temp = weight_goal // weight # 담을 수 있는 개수
            if temp > cnts: # temp만큼 없으면 cnts만큼 담기
                temp = cnts

            bag[i + 1][weight_goal] = max(bag[i][weight_goal - weight * temp] + value * temp, bag[i][weight_goal])

# for i in range(N + 1):
#     print(bag[i])

print(bag[N][M])
            



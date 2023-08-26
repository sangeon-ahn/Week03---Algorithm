N = int(input())
weights = list(map(int, input().split()))
K = int(input())
balls = list(map(int, input().split()))

dp = [[0] * ((30) * 500 + 1) for i in range(N + 1)]
result = set()

def recur(weight_idx, left_wights, right_weights):
    global N, weights

    # 왼쪽, 오른쪽 접시 무게간 차이의 무게를 구별할 수 있다.
    new_weights = abs(left_wights - right_weights)

    # 아직 결과셋에 들어오지 않은 무게라면 넣기
    if new_weights not in result:
        result.add(new_weights)

    # 끝에 도달했다면 리턴
    if weight_idx == N:
        return 0

    # 해당 idx 무게추까지 도달했을 때 아직 만들지 않았던 무게라면 진행
    if dp[weight_idx][new_weights] == 0:
        # 왼쪽에 idx번째 무게추 올리기
        recur(weight_idx + 1, left_wights + weights[weight_idx], right_weights)
        # 오른쪽에 idx번째 무게추 올리기
        recur(weight_idx + 1, left_wights, right_weights + weights[weight_idx])
        # 그냥 안올리기
        recur(weight_idx + 1, left_wights, right_weights)
        # dp에 해당 무게 만들 수 있다고 체크
        dp[weight_idx][new_weights] = 1

recur(0, 0, 0)

answer = []

for ball in balls:
    if ball in result:
        answer.append("Y")
    else:
        answer.append("N")

print(*answer)





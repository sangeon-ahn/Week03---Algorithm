N, K = map(int, input().split())
"""
dp[i]: i를 넣어서 만들 수 있는 최대 가치 
시간초과
메모이제이션 어케 적용함

"""
dp = [0] * (K + 1)
items = [list(map(int, input().split())) for _ in range(N)]
items.sort()

ans = 0
def recur(cnts, target, v_sum, w_sum):
    global ans
    if cnts >= N:
        return

    if w_sum > target:
        return
    
    if w_sum <= target:
        ans = max(ans, v_sum) 

    recur(cnts + 1, target, v_sum + items[cnts][1], w_sum + items[cnts][0])
    recur(cnts + 1, target, v_sum, w_sum)

recur(0, K, 0, 0)
print(ans)
    

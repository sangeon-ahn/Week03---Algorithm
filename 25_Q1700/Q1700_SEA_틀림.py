import sys
N, K = map(int, input().split())
order = list(map(int, input().split()))
multi_tap = []
use_cnts = [0] * (K + 1)
using = [False] * (K + 1)
"""
내 틀린 풀이: 빈도수 기준 가장 적은 빈도수인 콘센트를 뽑는 그리디
정답 그리디 풀이: 빈도수보다는 출현 시기를 기준으로 풀이해야 정상적으로 동작함을 확인할 수 있다
"""
# 제품 사용횟수 저장
for item in order:
    use_cnts[item] += 1

# 일단 멀티탭 채우기    
idx = 0
temp = 0
while temp < N and idx < K:
    # 해당 제품 사용중 아니면
    if not using[order[idx]]:
        # 멀티탭에 넣기
        multi_tap.append(order[idx])
        using[order[idx]] = True
        use_cnts[order[idx]] -= 1
        temp += 1
    # 사용중이었으면
    else:
        # use_cnts에서 1 빼주고
        use_cnts[order[idx]] -= 1
    # 다음 제품 확인하러 가기
    idx += 1

# 이렇게 하고 나왔는데 idx가 K면 끝
if idx == K:
    print(0) 

# 교체를 해야한다면
else:
    cnts = 0

    # idx번째 아이템부터 확인
    for i in range(idx, K):
        # 꼽혀있는 제품이면 패스
        if using[order[i]]:
            use_cnts[order[i]] -= 1
            continue

        # 그 외의 경우 뽑을 셀을 정한다.
        min_cell = sys.maxsize
        min_idx = -1

        # 멀티탭에 꼽힌 제품 중 가장 적게 사용될 제품을 고른다.
        for j in range(len(multi_tap)):
            if min_cell > use_cnts[multi_tap[j]]:
                min_cell = multi_tap[j]
                min_idx = j
        
        # 해당 제품과 교체한다.
        using[multi_tap[min_idx]] = False
        multi_tap[min_idx] = order[i]
        use_cnts[order[i]] -= 1
        using[order[i]] = True
        cnts += 1
    
    print(cnts)

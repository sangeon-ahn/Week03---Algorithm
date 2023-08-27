import sys
N, K = map(int, input().split())

# 멀티텝이 더 크면 교체할 필요 없어서 0 출력
if N >= K:
    print(0)
    sys.exit(0)

items_order = list(map(int, input().split()))

multi_tab = set()
cnts = 0

# 멀티텝에 꽂혀있는 제품 중 가장 나중에 꼽아야 할 제품을 반환한다.
def find_last(idx):
    max_item = 0
    max_item_idx = -1

    for item in multi_tab:
        try:
            temp_idx = items_order[idx:].index(item)
        except:
            temp_idx = K    
        
        if max_item_idx < temp_idx:
            max_item = item
            max_item_idx = temp_idx
    
    return max_item

for idx, num in enumerate(items_order):
    multi_tab.add(num)

    if len(multi_tab) > N:
        cnts += 1
        last_used_item = find_last(idx)
        multi_tab.discard(last_used_item)

print(cnts)
        
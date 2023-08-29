import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
    
visited = [0 for _ in range(k+1)]

queue = deque()
for coin in coins:
    if coin > k:
        continue;
    queue.append((coin,1))
    visited[coin ]= 1
    
flag = False;

while queue:
    val, cnt = queue.popleft()
    if val == k:
        print(cnt)
        flag = True
        break;
    for coin in coins:
        if val + coin > k:
            continue;
        if visited[val+coin] ==0:
            queue.append((val+cnt, cnt+1))
            visited[val+coin] = 1
            
if not flag:
    print(-1)
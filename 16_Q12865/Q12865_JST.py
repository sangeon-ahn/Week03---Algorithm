import sys
input = sys.stdin.readline

n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w: # 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
            d[i][j] = d[i-1][j]
        else: # 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v) #( 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.
                                                    #, 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.)

print(d[n][k])

'''
개수\무게 0  1  2  3  4  5  6   7
(0,0)  [0, 0, 0, 0, 0, 0, 0 , 0]
(6,13) [0, 0, 0, 0, 0, 0, 13, 13]
(4,8)  [0, 0, 0, 0, 8, 8, 13, 13]
(3,6)  [0, 0, 0, 6, 8, 8, 13, 14]
(5,12) [0, 0, 0, 6, 8, 12,13, 14]
'''

#참고 : https://hongcoding.tistory.com/50


'''
    [효율성]
    -메모리 : 227172 KB
    -시간 : 5840 ms
'''

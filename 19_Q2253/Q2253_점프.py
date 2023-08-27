import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
sm_rocks = set()
for _ in range(m):
    sm_rocks.add(int(input().rstrip()))

dp  = [[10001]* (int((2*n)**0.5)+2)  for _ in range(n+1)]
# y축은 돌, x축은 속도(칸)
#i번째 돌(y축)로 v(칸)의 속도(x축)로 왔을 때의 최솟값

'''
int((2*N)^0.5)의 의미
**1부터 속도가 끊임없이 1씩 증가하며 점프할 때 N에 도달했을 때의 속도의 근사값이다.**
-> 불필요한 연산을 막기 위한 연산

등차수열의 합 공식 = k(2a+(k-1)d) / 2
(이 문제에서 a(첫 번째 수) =1, d(공차) =1 )
따라서 마지막에 있는 돌까지 가장 빠르게 갈 수 있는 돌들의 수의 합 N
N = k(k+1)/2
k = (2N-k)^0.5 <= 2N^0.5
'''


dp[1][0] = 0
for i in range(2, n+1):
    if i in sm_rocks: #작은 돌일 때
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1
        #i-v 의 돌에서 x-1,x,x+1 중 최소


ans = min(dp[n])
if ans >= 10001:
    print(-1)
else:
    print(ans)


#참고 : https://velog.io/@grace0st/%EC%A0%90%ED%94%84-%EB%B0%B1%EC%A4%80-2253%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC


'''
    [효율성]
    -메모리 : 45960 KB
    -시간 : 640 ms
'''


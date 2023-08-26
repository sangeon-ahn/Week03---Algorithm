import sys
input = sys.stdin.readline

string = input().rstrip()
n = len(string)

#dp
dp = [[0] * n for _ in range(n)] #2차원 배열. y축과 x축 각각 문자열의 양 끝 점을 나타냄. 값이 1이면 양 끝점이 팰린드롬
'''
                                       A  B  A  B  A    => 문자열
    A에서 시작할 때                    A [1, 0, 1, 0, 1]    즉 1이 있는 A에서 시작할 때
    B에서 시작할 때                    B [0, 1, 0, 1, 0]
    A에서 시작할 때                    A [0, 0, 1, 0, 1]
    B에서 시작할 때                    B [0, 0, 0, 1, 0]
    A에서 시작할 때                    A [0, 0, 0, 0, 1]
'''
dp2 = [2500 for _ in range(n+1)] #최솟값을 찾아야 해서
dp2[-1] = 0 #start -1 때매


for num_len in range(n): #num_len = start와 end 사이 간격 ex) 1 : 0 / 121 : 2
    for start in range(n - num_len):
        end = start + num_len
        
        # 시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif string[start] == string[end]:
        	# 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end: dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start+1][end-1] == 1: dp[start][end] = 1
            

for end in range(n): #end : 몇칸짜리
    for start in range(end + 1):
        if dp[start][end]:
            dp2[end] = min(dp2[end], dp2[start - 1] + 1) #dp2[start - 1] + 1 : 이전 글자 까지의 집합 + 자기자신 추가
        else:
            dp2[end] = min(dp2[end], dp2[end - 1] + 1) # end - 1 : 이전꺼까지의 집합 + 자기자신 추가
'''
if 에서 dp2[start - 1] + 1 인 건 예를들어 ABABA 가 있고, start가 2, end 가 4 일 때, start - 1 만큼의 인덱스의 값(집합원소 수) + 자기 자신 1 이기 때문이다.
else 문에서 dp2[end - 1] + 1 인 이유는, 어차피 팰린드롬이 아니기에 마지막 원소는 이전 집합 + 1이기 때문이다.
'''

print(dp2[n - 1])


'''
    [효율성]
    -메모리 : 79416 KB
    -시간 : 3248 ms
'''
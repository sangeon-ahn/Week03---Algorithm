import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

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

for num_len in range(n): #num_len = start와 end 사이 간격 ex) 1 : 0 / 121 : 2
    for start in range(n - num_len):
        end = start + num_len
        
        # 시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif numbers[start] == numbers[end]:
        	# 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end: 
                dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start+1][end-1] == 1: 
                dp[start][end] = 1
            

#정답출력하기
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])


'''
    [효율성]
    -메모리 : 61956 KB
    -시간 : 2452 ms
'''
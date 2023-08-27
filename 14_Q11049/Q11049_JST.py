import sys
input = sys.stdin.readline

arr_list = []
n = int(input())
for _ in range(n):
    arr_list.append(list(map(int,input().rstrip().split(' '))))

dp = [[0]*n for _ in range(n)]  #아무것도 안 곱하는 상황은 연산이 0 이므로
#y축은 시작 행렬, x축은 끝 행렬

for term in range(1,n): #ex) 1이면 A,B or B,C / 2이면 A,B,C
    for start in range(n): # 첫행렬 : i, 끝행렬: i+term
        if start + term == n: # 범위를 벗어나면 무시
            break

        dp[start][start+term] = int(1e9) # 지금 계산할 첫행렬과 끝행렬

        for t in range(start, start+term): #t = 1 이면 A (B C)  // t = 2 이면 (A B) C
            dp[start][start+term] = min(dp[start][start+term], #기존것
                                        # 👇 왼쪽 묶음의 연산 횟수 + 오른쪽 묶음의 연산 횟수 + '왼쪽 묶음의 결과 행렬 X 오른쪽 묶음의 결과 행렬'의 연산 횟수
                                        dp[start][t]+dp[t+1][start+term] + arr_list[start][0] * arr_list[t][1] * arr_list[start+term][1])
            

print(dp[0][n-1])

#참고 : https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-11049-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-DP

'''
    pypy3
    [효율성]
    -메모리 : 117316 KB
    -시간 : 836 ms
'''






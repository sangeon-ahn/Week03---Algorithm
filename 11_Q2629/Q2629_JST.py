import sys
input = sys.stdin.readline
    
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
possible = [] # 가능한 무게(저울 차)
'''set을 쓰면 더 빠르다 : O(1)'''
dp = [[0]*15001 for i in range(n+1)] #dp[현재 몇번째 추를 사용할 차례인지][저울 무게의 차] = 0 : 더 진행 / 1 : 그만 진행

def scale(now,left,right,possible):
    new = abs(left-right) #new 는 양쪽 저울의 무게 차 , now는 현재 몇번째 추를 사용할 차례인지(인덱스)
    if(new not in possible):# 양쪽 저울의 무게 차 = 구슬의 무게
        possible.append(new)
    if(now == n):
        return 0
    if(dp[now][new] == 0): #0 : 더 진행 / 1 : 그만 진행
        # 저울의 왼쪽에 놓는경우
        scale(now+1,left+n_list[now],right,possible)

        # 저울의 오른쪽에 놓는경우
        scale(now+1,left,right+n_list[now],possible)

        # 저울에 아예 안놓는경우
        scale(now+1,left,right,possible)
        
        dp[now][new] = 1


scale(0,0,0,possible)

for i in range(0,len(m_list)):
    if(m_list[i] in possible):
        print("Y",end=' ')
    else:
        print("N",end=' ')


#참조 : https://source-sc.tistory.com/3

'''
    [효율성]
    -메모리 : 34300 KB
    -시간 : 312 ms
'''
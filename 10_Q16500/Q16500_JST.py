import sys

input = sys.stdin.readline

s = input().rstrip()
n = int(input())
a = []
for _ in range(n):
    a.append(input().rstrip())
dp = [0] * 101 #101 = 문자열의 최대 크기(100) + 1
#여기서 dp는 s의 어디까지 확인했나(무슨 단어까지 찾았나)이다. 한 단어를 찾으면 그 단어의 처음 글자 아래 1을 추가.
'''
    softwarecontest
    1000000010000001
    sol(0)  sol(8)
'''

result = 0
def sol(idx):
    global result
    if idx == len(s):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for i in range(len(a)):
        if len(s[idx:]) >= len(a[i]):
            for j in range(len(a[i])):
                if a[i][j] != s[idx+j]:
                    break
            else:
                sol(idx+len(a[i]))
    return
    
sol(0)
print(result)

'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 56 ms
'''
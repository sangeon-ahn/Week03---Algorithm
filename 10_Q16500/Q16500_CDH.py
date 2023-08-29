def sol(idx):
    global result
    if idx == len(string): # 정답
        result = 1
        return
    if dp[idx]: # 이미 검사한 경우 
        return
    dp[idx] = 1 # 검사했으니 1로 만들어 줌
    for i in range(len(numArr)):
        if len(string[idx:]) >= len(numArr[i]): # string가 numarr[i] 보다 더 길 때만 비교 가능 
            for j in range(len(numArr[i])): # numarr에 포함된 단어 길이 
                if numArr[i][j] != string[idx+j]: # numarr[i] 단어와 글자 하나하나 비교
                    break
            else:
                sol(idx+len(numArr[i]))
    return
    
string = input()
numArr = []
dp = [0] * 101 # 메모제이션 
for _ in range(int(input())):
    numArr.append(input())
result = 0
sol(0)
print(result)
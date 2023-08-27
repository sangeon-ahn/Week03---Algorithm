# expression = input().split('-')

# flag = False

# for ex in expression:
        

# print(expression)
"""
방법 1: 처음에 식 받을 때 - 기준으로 나눈 후, 길이가 1이면 다 더하기, 2 이상이면 처음 요소는 더해주고 이후부터는 다 빼주는데, 더하고 뺄 때는 + 기준으로 각 요소를 나눈 후 더한다.
방법 2: 식을 for문으로 순회하면서 숫자를 만들다가 -가 나오기 전까지는 다 더해주다가 -가 나오면 다 빼주는 식으로 하기
"""

# 방법 1로 해보기
expression = input().split('-')

ans = 0
temp = expression[0].split('+')
for num in temp:
    ans += int(num)

if len(expression) != 1:
    for i in range(1, len(expression)):        
        temp = expression[i].split('+')
        
        for num in temp:
            ans -= int(num)

print(ans)
            
    

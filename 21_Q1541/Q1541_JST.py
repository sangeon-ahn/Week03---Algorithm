'''
덧셈끼리 먼저 다 더한 후 뺄셈을 해준다.
ex) 3 + 4 - 3 - 10 + 24
    = 7   - 3 -   34
    =      -30
'''

import sys

sick = sys.stdin.readline().rstrip()
pluses = sick.split('-')
for i in range(len(pluses)):
    pluses[i] = sum(map(int,pluses[i].split('+')))
if len(pluses) == 1:
    print(pluses[0])
else:
    ans = pluses[0]
    for i in range(1,len(pluses)):
        ans -= pluses[i]
    print(ans)


'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 48 ms
'''
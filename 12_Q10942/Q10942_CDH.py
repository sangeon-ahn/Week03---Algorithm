import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)

M = int(input())
questions = [list(map(int,input().split())) for _ in range(M)]
print(questions)
def is_palindromes(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

for q in questions: # [[1,3], [2,5],[3,3], [5,7]]
    # print(q[0])
    if(is_palindromes("".join(map(str, arr[q[0]:q[1]+1:])))):
        print('1')
    else:
        print('0')
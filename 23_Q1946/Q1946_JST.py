'''
-문제 이해하기-

예제2를 서류심사 성적으로 정렬했을 때
서  면
1  4   -> 서류가 1등이므로 무조건 뽑힘. 면접의 최대 점수는 4
2  5   -> x
3  6   -> x
4  2   -> 서류가 1등인 애보다 면접 점수가 떨어지지 않으므로 붙임. 면접의 최대 점수는 2
5  7   -> x
6  1   -> 위에서 4번째 인 애보다 면접 점수가 떨어지지 않으므로 붙임. 면접의 최대 점수는 1
7  3   -> 바로 위 애보다 면접 점수도 떨어지고, 서류 점수도 떨어지므로 x
'''
import sys
input = sys.stdin.readline

tcase = int(input().rstrip())
for _ in range(tcase):
    n = int(input().rstrip())
    people = []
    for _ in range(n):
        people.append(list(map(int,input().rstrip().split())))
    people.sort()
    top = people[0][1]
    count = 1
    for i in range(1,len(people)):
        level = people[i][1]
        if level < top:
            top = level
            count+=1
    print(count)

'''
    [효율성]
    -메모리 : 50860 KB
    -시간 : 5928 ms
'''
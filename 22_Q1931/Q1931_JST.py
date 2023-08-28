import sys

n = int(sys.stdin.readline())

time = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s,e))

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:# 오름차순으로 정렬된 배열에서 다음 시간대의 시작 시간과 현재 시간대의 끝 시간을 비교.
        cnt += 1
        end_time = time[i][1]

print(cnt)

#참고 : https://suri78.tistory.com/26


'''
    [효율성]
    -메모리 : 52036 KB
    -시간 : 252 ms
'''
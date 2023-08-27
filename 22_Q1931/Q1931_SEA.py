N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
# 1순위: 끝나는 시간 기준 오름차순, 2순위: 시작시간 기준 오름차순
"""
시작시간 기준 오름차순 안하면 아래 반례 존재
4
3 3
2 3
1 3
2 2 
output
3
"""
meetings.sort(key = lambda x : (x[1], x[0]))

end_time = meetings[0][1]
cnts = 1
for i in range(1, len(meetings)):
    # 회의 데이터 뽑아서
    st, en = meetings[i]
    # 이전 회의 끝난 시간보다 시작시간이 더 작으면 패스
    if st < end_time:
        continue

    # 그 외에는 해당 회의를 진행하기
    end_time = en
    cnts += 1

print(cnts)

    

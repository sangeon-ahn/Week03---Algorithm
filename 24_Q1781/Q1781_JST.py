import heapq
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())  # 숙제의 개수
    problems = []  # 숙제 정보를 담는 최대힙. 값은 (데드라인, 컵라면 수) 튜플의 형태로 담긴다.
    cups = []  # 현재 시간에서 풀 수 있는 문제의 컵라면 수를 담아두는 최대힙
    time = 0  # 현재 시간

    for _ in range(N):
        deadline, cup = map(int, input().split())
        time = max(time, deadline)  # 현재 시간은 가장 큰 데드라인으로 설정한다.

        # problems에 (-deadline, cup)을 넣어둔다.
        # 최대힙으로 사용하기 위해 -deadline을 넣어줬다.
        heapq.heappush(problems, (-deadline, cup))

    res = 0  # 얻을 수 있는 컵라면의 총 개수
    while time > 0:
        while problems:  # 아직 풀 수 있는 숙제들이 남아있는 경우에만
            nextDeadline, nextCup = heapq.heappop(problems)

            # 만약 다음 숙제의 데드라인이 현재 시간과 일치한다면 해당 문제의 컵라면 수를
            # cups에 넣어준다. 이때 최대힙을 구성하기 위해 -nextCup의 형태로 값을 삽입한다.
            if time == -nextDeadline:
                heapq.heappush(cups, -nextCup)
            else:  # 만약 현재 시간에 풀 수 없는 문제라면 다시 problems에 넣어주고 반복문을 종료한다.
                heapq.heappush(problems, (nextDeadline, nextCup))
                break

        # 현재 시간에 풀 수 있는 문제가 있다면 문제를 풀고 컵라면을 얻는다.
        if cups:
            res += -heapq.heappop(cups)

        time -= 1

    print(res)


#참고 : https://one10004.tistory.com/246

'''
    [효율성]
    -메모리 : 61296 KB
    -시간 : 884 ms
'''
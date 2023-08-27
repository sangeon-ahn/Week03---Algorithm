T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort(key = lambda x: x[0])

    min_score = scores[0][1]
    cnts = 0
    for i in range(len(scores)):
        if min_score >= scores[i][1]:
            cnts += 1
            min_score = scores[i][1]
    
    answer.append(cnts)

for ans in answer:
    print(ans)


"""
220564kb	4740ms
"""
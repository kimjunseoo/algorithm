import math

n = int(input())

if n == 0:
    print(0)
else:
    scores = []

    for i in range(n):

        scores.append(int(input()))

    scores.sort()

    except_n = math.floor((n * 15 / 100) + 0.5)

    valid_scores = []

    for i in range(except_n, n - except_n):
        valid_scores.append(scores[i])

    print(math.floor((sum(valid_scores) / len(valid_scores)) + 0.5))
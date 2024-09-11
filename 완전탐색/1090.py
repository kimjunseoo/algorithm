#미해결

from itertools import *

checker_count = int(input())

checker_location = [list(map(int, input().split())) for _ in range(checker_count)]

for i in range(checker_count):
    if(i == 0):
        print(0)
        continue

    # i+1개가 모이는 조합
    comb = list(combinations(checker_location, i+1))
    
    min_distance = 0

    for j in comb:
        for k in range(i+1):
            x_distance = abs(j[k][0] - j[k+1][0])
            y_distance = abs(j[k][1] - j[k+1][1])
            total_distance = x_distance + y_distance

            if(total_distance < min_distance):
                min_distance = total_distance
    
    print(min_distance)
            
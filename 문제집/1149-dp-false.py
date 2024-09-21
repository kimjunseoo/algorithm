import copy

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

costs.insert(0, [0,0,0])

print("가격 :", costs)

answer = []

for j in range(3):

    dp = [ (0,0) for _ in range(N+1)]
    dp[1] = (costs[1][j], j)

    costs_sam = copy.deepcopy(costs)
    
    for i in range(2, N+1):

        before_color = dp[i-1][1]
        costs_sam[i][before_color] = 9999

        min_cost = min(costs_sam[i])
        min_cost_index = costs_sam[i].index(min_cost)
        dp[i] = (dp[i-1][0] + min_cost, min_cost_index)

        if i < N:
            costs_sam[i+1][min_cost_index] = 9999

    answer.append(dp[N][0])
    print(dp)
#print(answer)
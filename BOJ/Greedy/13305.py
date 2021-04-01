n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = 0
minCost = cost[0]
for i in range(n-1):
    minCost = min(minCost, cost[i])
    answer += distance[i]*minCost
print(answer)
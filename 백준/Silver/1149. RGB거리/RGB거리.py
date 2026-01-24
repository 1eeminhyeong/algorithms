n = int(input())

costs = [[0] * 3 for _ in range(1001)]

for i in range(1,n+1):
    costs[i] = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(1001)]

dp[1][0] = costs[1][0]
dp[1][1] = costs[1][1]
dp[1][2] = costs[1][2]

for i in range(2, n+1):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n][0], dp[n][1], dp[n][2]))
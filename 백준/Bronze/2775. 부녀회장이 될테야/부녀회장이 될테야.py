tc = int(input())

k = [0]*tc
n = [0]*tc

for i in range(tc):
    k[i] = int(input())
    n[i] = int(input())

room = max(n)+1
floor = max(k)+1

dp = [[0] * room for _ in range(floor)]

for i in range(1, room):
    dp[0][i] = i
for i in range(1, floor):
    dp[i][1] = 1

for i in range(1, floor):
    for j in range(1, room):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for i in range(tc):
    print(dp[k[i]][n[i]])
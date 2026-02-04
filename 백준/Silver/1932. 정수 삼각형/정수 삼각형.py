n = int(input())

dp = [[0] * n for _ in range(n)]
tri = [list(map(int, input().split())) for _ in range(n)]

dp[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            # 왼쪽 끝
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i:
            # 오른쪽 끝
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[n-1]))
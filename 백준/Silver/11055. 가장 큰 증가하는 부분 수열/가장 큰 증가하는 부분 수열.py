n = int(input())

seq = list(map(int, input().split()))
dp = seq[:]

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+seq[i])

print(max(dp))
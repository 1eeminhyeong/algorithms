n = int(input())

dp = [1]*n
seq = list(map(int, input().split()))

for i in range(n):
    for j in range(0, i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
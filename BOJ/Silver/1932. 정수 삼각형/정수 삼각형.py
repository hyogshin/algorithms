n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0] = tree[0][0]

if n > 1:
  dp[1][0] = dp[0] + tree[1][0]
  dp[1][1] = dp[0] + tree[1][1]

for i in range(2, n):
  dp[i][0] = dp[i-1][0] + tree[i][0]
  dp[i][i] = dp[i-1][i-1] + tree[i][i]

for i in range(2, n):
  for j in range(1, i):
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree[i][j]

if n == 1:
  print(tree[0][0])
else:
  print(max(dp[n-1]))
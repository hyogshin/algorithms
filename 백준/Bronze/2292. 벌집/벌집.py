n = int(input())

if n == 1:
  print(1)
else:
  dp = [0] * 18259
  dp[1] = 1

  for i in range(2, 18259):
    dp[i] = dp[i-1] + (6 * (i-1))

    if dp[i-1] < n and n <= dp[i]:
      print(i)
      break
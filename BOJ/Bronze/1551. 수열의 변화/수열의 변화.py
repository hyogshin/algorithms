n, k = map(int, input().split())
curr = list(map(int, input().split(',')))

for _ in range(k):
  nxt = []
  for i in range(len(curr) - 1):
    nxt.append(curr[i+1] - curr[i])
  curr = nxt

print(','.join(map(str, curr)))

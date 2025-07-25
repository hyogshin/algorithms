k, n = map(int, input().split())
ws = []
for _ in range(k):
  ws.append(int(input()))

right = max(ws)
left = 1
answer = 0
while right >= left:
  m = (right+left) // 2

  if sum(ws[i]//m for i in range(k)) < n:
    right = m - 1
  elif sum(ws[i]//m for i in range(k)) >= n:
    answer = m
    left = m + 1

print(answer)
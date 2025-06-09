from collections import deque
n, k = map(int, input().split())

q = deque()
rs = []
for i in range(1, n+1):
  q.append(i)

while q:
  for _ in range(k-1):
    q.append(q.popleft())
  rs.append(q.popleft())

print(f"<{', '.join(map(str, rs))}>")
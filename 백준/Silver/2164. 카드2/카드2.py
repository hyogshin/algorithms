from collections import deque 

n = int(input())

q = deque()
for i in range(1, n+1):
    q.append(i)

while q:
  if len(q) == 1:
    rs = q.popleft()
    print(rs)
    break

  q.popleft()
  a = q.popleft()
  q.append(a)
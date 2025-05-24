n = int(input())
ns = [list(map(int, input().split())) for _ in range(n)]
rs = []
cnt = 1

for i in range(n):
  for j in range(n):
    if i != j:
      if ns[i][0] < ns[j][0] and ns[i][1] < ns[j][1]:
        cnt += 1
  rs.append(cnt)
  cnt = 1

print(*rs)
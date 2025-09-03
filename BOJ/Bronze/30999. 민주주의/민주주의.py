n, m = map(int, input().split())

cnt = 0
for _ in range(n):
  o = 0
  opinions = input()
  for ch in opinions:
    if ch == 'O':
      o += 1
  
  if o > (m//2):
    cnt += 1

print(cnt)
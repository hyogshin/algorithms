n = int(input())
cnt = 0
for _ in range(n):
  s = input()
  if s[0] == 'C':
    cnt += 1

print(cnt)
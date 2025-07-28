n = int(input())
m = int(input())
s = list(input())

cnt = 0
# n -> (2*n + 1)
for i in range(m - 2*n):
  included = True
  for j in range(2*n + 1):
    if j % 2 == 0:
      if s[i+j] != 'I':
        included = False
        break
    else:
      if s[i+j] != 'O':
        included = False
        break

  if included:
    cnt += 1

print(cnt)
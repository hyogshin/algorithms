t = int(input())
for _ in range(t):
  total = 0
  s = input()
  for i in range(65, 91):
    if chr(i) not in s:
      total += i
  print(total)
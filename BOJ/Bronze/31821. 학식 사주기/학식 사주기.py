n = int(input())
menu = {}
for i in range(1, n + 1):
  menu[i] = int(input())

total = 0
m = int(input())
for _ in range(m):
  num = int(input())
  total += menu[num]

print(total)
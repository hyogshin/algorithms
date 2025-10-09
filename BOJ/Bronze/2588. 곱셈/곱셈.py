a = int(input())
b = input()

total = 0
for i in range(3):
  print(int(b[2 - i]) * a)
  total += (int(b[2 - i]) * a) * (10**i)

print(total)
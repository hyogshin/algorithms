even = 0
odd = 0

n = int(input())
k = input()

for digit in k:
  d = int(digit)
  if d == 0:
    even += 1
  elif d % 2 == 0:
    even += 1
  else:
    odd += 1

if even > odd:
  print(0)
elif even < odd:
  print(1)
else:
  print(-1)
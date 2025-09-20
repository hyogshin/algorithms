n = input()

contain = False
divisible = False
for d in n:
  if d == '7':
    contain = True

if int(n) % 7 == 0:
  divisible = True

if contain and divisible:
  print(3)
elif contain and not divisible:
  print(2)
elif not contain and divisible:
  print(1)
else:
  print(0)
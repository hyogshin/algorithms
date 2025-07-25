t = int(input())
ns = list(int(input()) for _ in range(t))

zero = [0] * (max(ns) + 2)
one = [0] * (max(ns) + 2)

for n in ns:
  zero[0] = 1
  zero[1] = 0
  one[0] = 0
  one[1] = 1

  for i in range(2, n+1):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]
  print(zero[n], one[n])
n = int(input())

def sum_of_m(m):
  return m + sum(int(d) for d in str(m))

for i in range(1, n+1):
  if sum_of_m(i) == n:
    print(i)
    break
else:
  print(0)
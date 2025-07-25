k = int(input())

ns = []
for _ in range(k):
  i = int(input())
  if i == 0 and ns:
    ns.pop()
  else:
    ns.append(i)

print(sum(ns))
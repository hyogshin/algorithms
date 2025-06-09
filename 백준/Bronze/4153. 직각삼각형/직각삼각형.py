while 1:
  ns = list(map(int, input().split()))

  if ns[0] == 0 and ns[1] == 0 and ns[2] == 0:
    break
  m = max(ns)
  ns.remove(m)

  if m**2 == ns[0]**2 + ns[1]**2:
    print('right')
  else:
    print('wrong')
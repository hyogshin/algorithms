k = False
l = False
p = False

for _ in range(3):
  s = input()
  if s[0] == 'k':
    k = True
  elif s[0] == 'l':
    l = True
  elif s[0] == 'p':
    p = True

if k and l and p:
  print('GLOBAL')
else:
  print('PONIX')
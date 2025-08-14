groups = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
groups += [g.lower() for g in groups]

while True:
  encoded = input()
  if encoded == '#':
    break
  
  decoded = []
  for i, ch in enumerate(encoded, start=1):
    for g in groups:
      if ch in g:
        l = len(g)
        idx = g.index(ch)
        decoded.append(g[(idx-i)%l])
  print(''.join(decoded))
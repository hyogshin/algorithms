t = int(input())
for i in range(t):
  n = int(input())
  round = ''
  if n <= 25:
    round = 'World Finals'
  elif n <= 1000:
    round = 'Round 3'
  elif n <= 4500:
    round = 'Round 2'
  else:
    round = 'Round 1'
  print(f'Case #{i+1}: {round}')
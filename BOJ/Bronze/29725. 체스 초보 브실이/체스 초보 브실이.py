rubric = {'K': 0, 'P': 1, 'N': 3, 'B':3, 'R': 5, 'Q': 9}
for key, val in list(rubric.items()):
  rubric[key.lower()] = val

board = [input() for _ in range(8)]
score = 0
for row in board:
  for ch in row:
    if ch == '.':
      continue
    if ch.isupper():
      score += rubric[ch]
    else:
      score -= rubric[ch]
print(score)
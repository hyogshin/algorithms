n, k = map(int, input().split())
g = list(map(int, input().split()))
grades = []

for i in range(k):
  p = (g[i] * 100) // n
  if p <= 4:
    grades.append(1)
  elif p <= 11:
    grades.append(2)
  elif p <= 23:
    grades.append(3)
  elif p <= 40:
    grades.append(4)
  elif p <= 60:
    grades.append(5)
  elif p <= 77:
    grades.append(6)
  elif p <= 89:
    grades.append(7)
  elif p <= 96:
    grades.append(8)
  else:
    grades.append(9)

print(*grades)
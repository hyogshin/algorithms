m = 0
auditorium = ''
for _ in range(7):
  name, applicants = input().split()
  m = max(int(applicants), m)
  if m == int(applicants):
    auditorium = name

print(auditorium)
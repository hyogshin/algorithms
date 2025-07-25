students = [int(input()) for i in range(28)]

rs = []
for i in range(1, 31):
  rs.append(i)

for i in range(31):
  if i in students:
    rs.remove(i)

for i in range(len(rs)):
  print(rs[i])

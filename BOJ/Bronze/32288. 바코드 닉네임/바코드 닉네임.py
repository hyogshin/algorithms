n = int(input())
barcode = input()

rs = []
for d in barcode:
  if d.isupper():
    rs.append(d.lower())
  elif d.islower():
    rs.append(d.upper())

print(''.join(rs))
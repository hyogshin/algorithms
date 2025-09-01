s = input()
rs = []
rs.append(s[0])
for i, k in enumerate(s):
  if i > 0:
    if k == s[i-1]:
      continue
    else:
      rs.append(k)

print(''.join(rs))
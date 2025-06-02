n = int(input())

def balance(s):
  chk = []
  for i in  s:
    if i == '(' or i == '[':
      chk.append(i)
    elif i == ')':
      if chk and chk[-1] == '(':
        chk.pop()
      else: return 'NO'
    elif i == ']':
      if chk and chk[-1] == '[':
        chk.pop()
      else: return 'NO'

  if not chk:
    return 'YES'
  else:
    return 'NO'

for i in range(n):
  l = input()
  print(balance(l))
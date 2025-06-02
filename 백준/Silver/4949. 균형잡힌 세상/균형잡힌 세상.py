def balance(s):
  stack = []
  for i in s:
    if i == '(':
      stack.append(i)
    elif i == '[':
      stack.append(i)
    elif i == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else: return 'no'
    elif i == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else: return 'no'
    # elif i == '.':
    #   break

  return 'yes' if not stack else 'no'

while 1:
  s = input()
  if s == '.':
    break
  print(balance(s))
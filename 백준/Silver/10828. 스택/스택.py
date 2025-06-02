n = int(input())
stack = []
for i in range(n):
  c = input().split()
  if c[0] == 'push':
    stack.append(c[1])
  elif c[0] == 'pop':
    print(-1) if not stack else print(stack.pop())
  elif c[0] == 'size':
    print(len(stack))
  elif c[0] == 'empty':
    print(1) if not stack else print(0)
  elif c[0] == 'top':
    print(-1) if not stack else print(stack[-1])
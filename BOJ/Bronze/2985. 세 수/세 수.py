import operator

a, b, c = map(int, input().split())
ops = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.floordiv
}

for symbol, func in ops.items():
  if func(a, b) == c:
    print(f'{a}{symbol}{b}={c}')
    break
  elif a == func(b, c):
    print(f'{a}={b}{symbol}{c}')
    break
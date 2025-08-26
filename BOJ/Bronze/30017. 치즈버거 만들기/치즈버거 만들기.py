a, b = map(int, input().split())

if a > b:
  a = b + 1
else:
  b = a - 1
  
print(a + b)

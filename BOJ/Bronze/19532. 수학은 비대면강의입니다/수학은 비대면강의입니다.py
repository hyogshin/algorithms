a, b, c, d, e, f = map(int, input().split())
A, B, C, D, E, F = a*d, b*d, c*d, d*a, e*a, f*a

if B-E != 0 and A != 0:
  y = (C-F)//(B-E)
  x = (C-(B*y))//A
elif a == 0:
  y = c//b
  x = (f - (e*y)) // d
elif d == 0:
  y = f//e
  x = (c - (b*y)) // a
elif B-E == 0:
  x = (C-F)//(A-D)
  y = (C - A*x) // B


print(x, y)
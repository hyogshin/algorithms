import sys
input = sys.stdin.readline
n = int(input().rstrip())

m0, m1, m2 = map(int, input().rstrip().split())
mi0, mi1, mi2 = m0, m1, m2

if n > 1:
  for i in range(n-1):
    a, b, c = map(int, input().rstrip().split())
    ma0, mii0 = max(m0, m1), min(mi0, mi1)
    ma1, mii1 = max(m0, m1, m2), min(mi0, mi1, mi2)
    ma2, mii2 = max(m1, m2), min(mi1, mi2)

    m0 = ma0 + a
    m1 = ma1 + b
    m2 = ma2 + c
    
    mi0 = mii0 + a
    mi1 = mii1 + b
    mi2 = mii2 + c

print(max(m0, m1, m2), min(mi0, mi1, mi2))
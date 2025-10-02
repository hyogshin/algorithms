m = list(map(int, input().split()))
n = int(input())

scholarship = 0
for _ in range(n):
  b, l, s = input().split()
  b, s = int(b), int(s)
  l = float(l)
  
  if l >= 2.0 and s >= 17:
    scholarship += m[b]

print(scholarship)
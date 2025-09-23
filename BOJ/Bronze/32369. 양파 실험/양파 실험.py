n, a, b = map(int, input().split())

complimented = 1
criticized = 1

for _ in range(n):
  complimented += a
  criticized += b

  if criticized > complimented:
    tmp = criticized
    criticized = complimented
    complimented = tmp
  
  if criticized == complimented:
    criticized -= 1

print(complimented, criticized)
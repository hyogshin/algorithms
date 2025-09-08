n = int(input())
appeared = False

if 1 <= n < 10:
  appeared = True

for i in range(2, 10):
  for j in range(1, 10):
    if n == i * j:
      appeared = True
      break
  
print(1 if appeared else 0)
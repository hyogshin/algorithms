exp = [0] * 3
print(exp)

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
      break
    else:
      if min(a, b, c)**2 + med(a,b,c)**2 == max(a, b, c)**2:
        print('right')
      else:
        print('wrong')
      

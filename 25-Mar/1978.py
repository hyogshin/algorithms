cnt = int(input())
ns = input().split()

n = 0

for i in ns:
  if int(i) == 1 or int(i) == 0:
    continue
  elif int(i)//2 > 1 and int(i)%2 == 0:
    continue
  elif int(i)//3 > 1 and int(i)%3 == 0:
    continue
  elif int(i)//5 > 1 and int(i)%5 == 0:
    continue
  elif int(i)//7 > 1 and int(i)%7 == 0:
    continue
  elif int(i)//11 > 1 and int(i)%11 == 0:
    continue
  elif int(i)//13 > 1 and int(i)%13 == 0:
    continue
  elif int(i)//17 > 1 and int(i)%17 == 0:
    continue
  elif int(i)//19 > 1 and int(i)%19 == 0:
    continue
  elif int(i)//23 > 1 and int(i)%23 == 0:
    continue
  elif int(i)//29 > 1 and int(i)%29 == 0:
    continue
  elif int(i)//31 > 1 and int(i)%31 == 0:
    continue
  else:
    n += 1


print(n)
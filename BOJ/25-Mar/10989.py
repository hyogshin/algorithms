cnt = int(input())
lns =  [0] * cnt

for i in range(cnt):
  lns[i] = int(input())

lns.sort()

for i in lns:
  print(i)
# for i in range(cnt):
#   mini = lns.pop(lns.index(min(lns)))
#   print(mini)
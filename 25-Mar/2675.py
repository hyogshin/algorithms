cnt = int(input())
lns = [0] * cnt


for i in range(cnt):
  lns[i] = input().split()

for i in range(len(lns)):
  answer = [0] * len(lns[i][1])
  for j in range(len(lns[i][1])):
    answer[j] = lns[i][1][j]*int(lns[i][0])
  print(''.join(answer))

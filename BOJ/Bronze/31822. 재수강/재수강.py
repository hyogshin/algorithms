retake = input()
n = int(input())
cnt = 0
for _ in range(n):
  code = input()
  same = True
  for i, ch in enumerate(retake):
    if i == 5:
      if same == True:
        cnt += 1
      break
    if ch != code[i]:
      same = False

print(cnt)
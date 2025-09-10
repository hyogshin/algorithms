retake = input()
n = int(input())
cnt = 0
for _ in range(n):
  code = input()
  if retake[:5] == code[:5]:
    cnt += 1

print(cnt)
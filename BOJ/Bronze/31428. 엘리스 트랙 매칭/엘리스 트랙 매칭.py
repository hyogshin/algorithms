n = int(input())
tracks = input().split()
track = input()

cnt = 0
for t in tracks:
  if t == track:
    cnt += 1

print(cnt)
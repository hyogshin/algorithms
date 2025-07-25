cnt = int(input())
score = list(map(int, input().split()))
total = 0
print(score)
for i in score:
  total += (i/max(score)*100)


print(total/cnt)
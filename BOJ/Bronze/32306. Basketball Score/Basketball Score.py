score = [0] * 3
for i in range(1, 3):
  one, two, three = map(int, input().split())
  score[i] = one * 1 + two * 2 + three * 3

print(0 if score[1] == score[2] else score.index(max(score)))
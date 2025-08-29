n = int(input())
suspects = [input() for _ in range(n)]

for suspect in suspects:
  if 'S' in suspect:
    print(suspect)
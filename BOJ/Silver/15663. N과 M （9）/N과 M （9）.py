n, m = map(int, input().split())
ns = list(map(int, input().split()))
used = [False] * n
ns.sort()

def backtrack(arr):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  prev = -1
  for i in range(n):
    if not used[i] and prev != ns[i]:
      prev = ns[i]
      used[i] = True
      arr.append(ns[i])
      backtrack(arr)
      arr.pop()
      used[i] = False

backtrack([])
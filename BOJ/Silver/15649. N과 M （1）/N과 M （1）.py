n, m = map(int, input().split())
marked = [False] * (n+1)
rs = []

def backtrack():
  if len(rs) == m:
    print(*rs)
    return
  

  for i in range(1, n+1):
    if not marked[i]:
      marked[i] = True
      rs.append(i)
      
      backtrack()

      rs.pop()
      marked[i] = False


backtrack()
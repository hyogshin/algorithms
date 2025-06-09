import sys
input = sys.stdin.readline
m = int(input())

rs = set()
for _ in range(m):
  cmd = input().strip().split()
  if cmd[0] == 'add':
    rs.add(int(cmd[1]))
  elif cmd[0] == 'remove':
    rs.discard(int(cmd[1]))
  elif cmd[0] == 'check':
    print(1 if int(cmd[1]) in rs else 0)
  elif cmd[0] == 'toggle':
    if int(cmd[1]) in rs:
      rs.remove(int(cmd[1]))
    else:
      rs.add(int(cmd[1]))
  elif cmd[0] == 'all':
    rs = set(range(1, 21))
  elif cmd[0] == 'empty':
    rs.clear()
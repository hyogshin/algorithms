import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
ps = [input().rstrip() for _ in range(n)]
    
for _ in range(m):
  i = input().rstrip()
  if i.isdigit():
    print(ps[int(i)-1])
  else:
    print(ps.index(i)+1)
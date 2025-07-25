import sys
input = sys.stdin.readline

n = int(input())
l = [tuple(input().split()) for i in range(n)]

for a, b in sorted(l, key = lambda x: int(x[0])):
  print(a, b)
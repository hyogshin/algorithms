import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ns = [int(input()) for _ in range(n)]
ns.sort()
q = deque(ns)

outlier = int(n*(0.15)+0.5)

for i in range(outlier):
  q.pop()
  q.popleft()

if len(q) == 0:
  print(0)
else:
  print(int(sum(i for i in q)/len(q)+0.5))
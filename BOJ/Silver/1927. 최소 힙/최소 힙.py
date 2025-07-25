import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input().rstrip())
for _ in range(n):
  i = int(input().rstrip())
  if i == 0:
    print(heapq.heappop(heap) if heap else 0)
  else:
    heapq.heappush(heap, i)
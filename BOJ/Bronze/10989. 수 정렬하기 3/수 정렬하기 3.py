import sys
input = sys.stdin.readline

n = int(input().rstrip('\n'))

ns = [0] * 10001

for _ in range(n):
  i = int(input().rstrip('\n'))
  ns[i] += 1

for i in range(1, 10001):
  for j in range(ns[i]):
    print(i)
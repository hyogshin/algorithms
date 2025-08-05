import sys
input = sys.stdin.readline

while True:
  n, m = map(int, input().rstrip().split())

  if n == 0 and m == 0:
    break

  ns = set(int(input().rstrip()) for _ in range(n))
  ms = set(int(input().rstrip()) for _ in range(m))

  print(len(ns & ms))

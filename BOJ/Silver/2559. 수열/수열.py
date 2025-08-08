n, k = map(int, input().split())
temps = list(map(int, input().split()))

s = sum(temps[:k])
m = s
for left in range(n - k):
  s -= temps[left]
  s += temps[left + k]
  m = max(m, s)

print(m)
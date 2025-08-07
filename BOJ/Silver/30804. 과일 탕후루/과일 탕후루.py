from collections import defaultdict

n = int(input())
ns = list(map(int, input().split()))

m = 0
left = 0
counter = defaultdict(int)

for right in range(n):
  counter[ns[right]] += 1

  while len(counter) > 2:
    counter[ns[left]] -= 1
    if counter[ns[left]] == 0:
      del counter[ns[left]]
    left += 1
  
  m = max(m, right - left + 1)
  
print(m)
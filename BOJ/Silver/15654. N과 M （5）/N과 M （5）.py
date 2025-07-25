n, m = map(int, input().split())
ns = list(map(int, input().split()))
ns.sort()

def permutation(arr, n, m, ns):
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  
  for i in ns:
    if i not in arr:
      arr.append(i)
      permutation(arr, n, m, ns)
      arr.pop()

permutation([], n, m, ns)
n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

ns.sort()

def exists(arr, target):
  l, h = 0, len(ns) -1
  while l <= h:
    mid = (l+h) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target:
      l = mid + 1
    else:
      h = mid - 1
  return False


for i in ms:
  print(1 if exists(ns, i) else 0)
x, y, w, h = map(int, input().split())
comparison = [x, y, w-x, h-y]
rs = min(comparison)
print(rs)
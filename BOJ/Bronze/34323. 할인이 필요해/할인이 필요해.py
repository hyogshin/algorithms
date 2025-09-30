n, m, s = map(int, input().split())

print(min((m + 1) * s * (100 - n) // 100, m * s))
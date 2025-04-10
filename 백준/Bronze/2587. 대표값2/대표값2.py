ns = [int(input()) for _ in range(5)]

avg = int(sum(ns)/5)
md = sorted(ns)[2]

print(avg)
print(md)
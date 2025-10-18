from collections import Counter

l = int(input())
s = input()
cnt = Counter(s)

a = cnt['A']
c = cnt['C']
g = cnt['G']
t = cnt['T']

print((a*c*g*t) % 1000000007)
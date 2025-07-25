import sys
input = sys.stdin.readline

n = int(input())
ns = [int(input()) for _ in range(n)]
ns.sort()
print(*ns, sep='\n')
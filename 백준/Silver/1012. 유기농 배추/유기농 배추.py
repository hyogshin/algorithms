import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if not marked[nx][ny] and graph[nx][ny] == 1:
                marked[nx][ny] = True
                dfs(nx, ny)

t = int(input())
rs = []
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        i, j = map(int, input().split())
        graph[i][j] = 1

    marked = [[False] * n for _ in range(m)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if not marked[i][j] and graph[i][j] == 1:
                marked[i][j] = True
                dfs(i, j)
                cnt += 1

    rs.append(cnt)

print('\n'.join(map(str, rs)))

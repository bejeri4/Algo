# https://atcoder.jp/contests/dp/tasks/dp_g

p = 1000000007

n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append([0] * m)
    line = input()
    for j in range(m):
        if line[j] == "#":
            grid[i][j] = -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == -1:
            continue
        if i == 0 and j == 0:
            grid[i][j] = 1
        elif i == 0:
            grid[i][j] = grid[i][j - 1]
        elif j == 0:
            grid[i][j] = grid[i - 1][j]
        elif grid[i - 1][j] == -1 and grid[i][j - 1] == -1:
            grid[i][j] = -1
        elif grid[i - 1][j] == -1:
            grid[i][j] = grid[i][j - 1]
        elif grid[i][j - 1] == -1:
            grid[i][j] = grid[i - 1][j]
        else:
            grid[i][j] = (grid[i - 1][j] + grid[i][j - 1]) % p


print(grid[-1][-1] if grid[-1][-1] != -1 else 0)

# https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1):
    arr[i][0] = arr[i][0] + max(arr[i + 1][1], arr[i + 1][2])
    arr[i][1] = arr[i][1] + max(arr[i + 1][0], arr[i + 1][2])
    arr[i][2] = arr[i][2] + max(arr[i + 1][0], arr[i + 1][1])

print(max(arr[0]))

# https://atcoder.jp/contests/dp/tasks/dp_f

import math

a = input()
b = input()

dp = [None] * len(a)

for i in range(len(a) - 1, -1, -1):
    dp[i] = [""] * len(b)
    for j in range(len(b) - 1, -1, -1):
        horiz = ""
        vert = ""
        diag = ""
        if i <= len(a) - 2 and j <= len(b) - 2:
            diag = dp[i + 1][j + 1]
        if i <= len(a) - 2:
            horiz = dp[i + 1][j]
        if j <= len(b) - 2:
            vert = dp[i][j + 1]
        if a[i] == b[j]:
            diag = a[i] + diag
        maxLen = max(len(horiz), len(vert), len(diag))
        if maxLen == len(horiz):
            dp[i][j] = horiz
        elif maxLen == len(vert):
            dp[i][j] = vert
        if maxLen == len(diag):
            dp[i][j] = diag

print(dp[0][0])

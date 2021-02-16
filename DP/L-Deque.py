# https://atcoder.jp/contests/dp/tasks/dp_l

n = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(n):
    dp.append([[0, 0]] * n)
    dp[i][i] = [arr[i], 0]

for s in range(1, n):
    i = 0
    j = s
    while i < n and j < n:
        player1V1 = arr[i] + dp[i + 1][j][1]
        player1V2 = arr[j] + dp[i][j - 1][1]
        if player1V1 > player1V2:
            player2 = dp[i + 1][j][0]
            dp[i][j] = [player1V1, player2]
        else:
            player2 = dp[i][j - 1][0]
            dp[i][j] = [player1V2, player2]

        i += 1
        j += 1

print(dp[0][-1][0] - dp[0][-1][1])

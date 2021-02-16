# https://atcoder.jp/contests/dp/tasks/dp_k

first = "First"
second = "Second"

n, k = map(int, (input().split()))
arr = list(map(int, input().split()))
arr.sort()

dp = [second] * (k + 1)
for elem in arr:
    if elem < k + 1:
        dp[elem] = first


for i in range(k + 1):
    if dp[i] == first:
        continue
    for elem in arr:
        if i - elem >= 0:
            if dp[i - elem] == second:
                dp[i] = first
                break
        else:
            break

print(dp[-1])

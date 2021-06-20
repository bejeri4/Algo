def rec(s, memo):
    if s in memo:
        return memo[s]
    if s == "":
        return 1
    if s[0] == "0":
        return 0
    result = rec(s[1:], memo)
    if len(s) > 1 and int(s[:2]) <= 26:
        result += rec(s[2:], memo)
    memo[s] = result
    return result


class Solution:
    def numDecodings(self, s: str) -> int:
        return rec(s, dict())

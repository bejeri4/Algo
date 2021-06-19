class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                balance -= 1
                if balance == -1:
                    balance = 0
                    s = s[:i] + s[i + 1:]
                    continue
            i += 1
        i = len(s) - 1
        while balance > 0:
            if s[i] == "(":
                balance -= 1
                s = s[:i] + s[i + 1:]
            i -= 1
        return s

def isDigit(ch):
	return ord(ch) >= ord("0") and ord(ch) <= ord("9")


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        sign = 1
        result = 0
        operand = 0
        for ch in s:
            if isDigit(ch):
                operand = (operand * 10) + int(ch)
            elif ch == "+":
                result += sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                result += sign * operand
                sign = -1
                operand = 0
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ch == ")":
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                operand = 0
        return result + sign * operand


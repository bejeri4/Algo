# https://www.interviewbit.com/problems/fraction/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        if A == None or not B:
            return None
        if A % B == 0:
            return str(A // B)
        result = ""
        if (A < 0 and B > 0) or (A > 0 and B < 0):
            result += "-"
        A = abs(A)
        B = abs(B)
        result += str(A // B)
        A = A % B
        result += "."
        prevDivisors = dict()
        i = len(result)
        while True:
            if A == 0:
                return result
            A *= 10
            div = A // B
            rem = A % B
            result += str(div)
            if A in prevDivisors:
                j = len(result) - 1
                while i >= 1:
                    if result[j] != result[j - 1]:
                        break
                    j -= 1
                result = result[:i + 1]
                index = prevDivisors[A]
                result = result[:index] + "(" + result[index:-1] + ")"
                return result
            prevDivisors[A] = i
            A = rem
            i += 1
            

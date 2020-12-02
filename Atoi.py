# https://www.interviewbit.com/problems/atoi/

maxInt = pow(2, 31) - 1
minInt = -pow(2, 31)

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()
        resStr = ""
        isNegative = False
        if A != "" and A[0] == "-":
            isNegative = True
            A = A[1:]
        elif A != "" and A[0] == "+":
            A = A[1:]
        for i in range(len(A)):
            if ord(A[i]) - ord("0") >= 0 and ord(A[i]) - ord("0") <= 9:
                resStr += A[i]
            else:
                break
        result = 0
        for ch in resStr:
            result = result * 10 + int(ch)
        if isNegative:
            result = -result
        if result > maxInt:
            return maxInt
        if result < minInt:
            return minInt
        return result

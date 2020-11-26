# https://www.interviewbit.com/problems/power-of-two-integers/

def isPower(A, i):
    num = i
    while True:
        num *= i
        if num == A:
            return True
        if num > A:
            return False

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        root = int(math.sqrt(A))
        for i in range(2, root + 1):
            if isPower(A, i):
                return 1
        return 0

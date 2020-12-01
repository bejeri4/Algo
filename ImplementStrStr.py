# https://www.interviewbit.com/problems/implement-strstr/

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if not B or B == "":
            return 0
        for i in range(len(A) - len(B) + 1):
            if B == A[i:i + len(B)]:
                return i
        return -1

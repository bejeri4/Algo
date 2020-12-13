# https://www.interviewbit.com/problems/3-sum/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if not A or len(A) < 3:
            return 0
        A.sort()
        result = A[0] + A[1] + A[2]
        curIndex = 0
        while curIndex < len(A):
            curElem = A[curIndex]
            i = curIndex + 1
            j = len(A) - 1
            while i < j:
                s = curElem + A[i] + A[j]
                if s > B:
                    j -= 1
                elif s < B:
                    i += 1
                else:
                    return B
                if abs(s - B) < abs(result - B):
                    result = s
            curIndex += 1
        return result

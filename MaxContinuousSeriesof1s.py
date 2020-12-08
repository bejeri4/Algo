# https://www.interviewbit.com/problems/max-continuous-series-of-1s/

import queue

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        s = 0
        e = 0
        flippedIndices = queue.Queue()
        maxLen = 0
        oldestIndex = 0
        for i in range(len(A)):
            if A[i] == 0:
                flippedIndices.put(i)
                if B > 0:
                    B -= 1
                else:
                    oldestIndex = flippedIndices.get(i) + 1
            curLen = i - oldestIndex + 1
            if curLen > maxLen:
                maxLen = curLen 
                s = oldestIndex
                e = i
        result = []
        for i in range(s, e + 1):
            result.append(i)
        return result

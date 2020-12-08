# https://www.interviewbit.com/problems/maximum-ones-after-modification/

import queue

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if not A or len(A) == 0:
            return 0
        result = 0
        usedFlips = 0
        flippedIndices = queue.Queue()
        i = 0
        curSegmentLength = 0
        while i < len(A):
            if A[i] == 1:
                curSegmentLength += 1
            else:
                flippedIndices.put(i)
                if usedFlips < B:
                    usedFlips += 1
                    curSegmentLength += 1
                else:
                    oldestIndex = flippedIndices.get()
                    curSegmentLength = i - oldestIndex
            if curSegmentLength > result:
                result = curSegmentLength
            i += 1
        return result

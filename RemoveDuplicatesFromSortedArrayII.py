# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return 2
        i = 0
        j = 0
        while i < len(A) and j < len(A):
            numRemoved = 0
            while j < len(A) and A[i] == A[j]:
                j += 1
            if j - i >= 3:
                del A[i: j - 2]
                numRemoved = j - i + 2
            j -= numRemoved
            i = j
        return len(A)

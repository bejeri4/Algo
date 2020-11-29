# https://www.interviewbit.com/problems/allocate-books/

def canRead(A, B, maxPages):
    curStrudent = 0
    i = 0
    B -= 1
    while i < len(A):
        if A[i] > maxPages:
            return False
        if curStrudent + A[i] > maxPages:
            B -= 1
            curStrudent = 0
        curStrudent += A[i]
        i += 1
        
    return B >= 0
        
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B > len(A):
            return -1
        i = 0
        j = 0
        result = -1
        for elem in A:
            j += elem
        while i <= j:
            mid = i + (j - i) // 2
            if canRead(A, B, mid):
                result = mid
                j = mid - 1
            else:
                i = mid + 1
        return result

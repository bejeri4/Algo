# https://www.interviewbit.com/problems/first-missing-integer/

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            elem = A[i]
            if elem == i + 1:
                continue
            if elem > 0 and elem <= len(A):
                if A[elem - 1] != elem:
                    swap(A, elem - 1, i)
                    i -= 1
                    
        for i in range(len(A)): 
            if A[i] != i + 1:
                return i + 1
        return len(A) + 1

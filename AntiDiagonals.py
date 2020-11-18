# https://www.interviewbit.com/problems/anti-diagonals/

def getDiag(matrix, i, j):
    result = []
    while i < len(matrix) and j >= 0:
        result.append(matrix[i][j])
        i += 1
        j -= 1
    return result

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        result = []
        for i in range(len(A)):
            result.append(getDiag(A, 0, i))
        for i in range(1, len(A)):
            result.append(getDiag(A, i, len(A) - 1))
        return result

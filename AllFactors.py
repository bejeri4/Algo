# https://www.interviewbit.com/problems/all-factors/

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A == 1:
            return [1]
        result = []
        for i in range(1, int(math.sqrt(A)) + 1):
            if A % i == 0:
                result.append(i)
        couples = []
        for i in range(len(result) - 1, -1, -1):
            if result[i] * result[i] != A:
                couples.append(A // result[i])
        return result + couples

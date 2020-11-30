# https://www.interviewbit.com/problems/different-bits-sum-pairwise/

p = 1000000007

def addBitsToIndices(arr, elem):
    i = len(arr) - 1
    while elem != 0:
        arr[i] += elem % 2
        elem //= 2
        i -= 1

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        arr = [0] * 32
        for elem in A:
            addBitsToIndices(arr, elem)
        result = 0
        for cnt in arr:
            result += (cnt * (len(A) - cnt)) * 2 % p
            result %= p
        return result

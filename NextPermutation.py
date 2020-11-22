# https://www.interviewbit.com/problems/next-permutation/

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def reverse(A, startIndex):
    i = startIndex
    j = len(A) - 1
    while i <= j:
        swap(A, i, j)
        i += 1
        j -= 1

def indexOfNextGreater(A, start):
    nextGreater = math.inf
    result = -1
    for i in range(start + 1, len(A)):
        if A[i] < nextGreater and A[i] > A[start]:
            result = i
            nextGreater = A[i]
    return result

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        if len(A) < 2:
            return A
        swapIndex = -1
        for i in range(len(A) - 1, 0, -1):
            if A[i] > A[i - 1]:
                swapIndex = i - 1
                break
        if swapIndex == -1:
            reverse(A, 0)
        else:
            swap(A, swapIndex, indexOfNextGreater(A, swapIndex))
            reverse(A, swapIndex + 1)
        return A

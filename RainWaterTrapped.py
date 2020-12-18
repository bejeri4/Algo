# https://www.interviewbit.com/problems/rain-water-trapped/

def fillNextNotSmallers(A, arr):
    stack = []
    for i in range(len(arr)):
        elem = A[i]
        while True:
            if not stack:
                break
            prev = stack.pop()
            if elem >= prev[1]:
                arr[prev[0]] = i
            else:
                stack.append(prev)
                break
        stack.append((i, elem))
        
        
def greatestElemIndex(arr, startIndex):
    maxElem = -math.inf
    ind = 0
    for i in range(startIndex, len(arr)):
        if arr[i] > maxElem:
            maxElem = arr[i]
            ind = i
    return ind


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if len(A) < 3:
            return 0
        nextNotSmallers = [-1] * len(A)
        fillNextNotSmallers(A, nextNotSmallers)
        result = 0
        i = 0
        canUsePrev = False
        while i < len(nextNotSmallers):
            j = nextNotSmallers[i]
            if j == -1:
                i += 1
                canUsePrev = True
                continue
            else:
                height = A[i]
                if canUsePrev:
                    i -= 1
                    j = greatestElemIndex(A, i + 1)
                    height = A[j]
                distance = (j - i - 1)
                result += height * distance
                for h in A[i + 1: j]:
                    result -= h
                i = j
                canUsePrev = False
        return result

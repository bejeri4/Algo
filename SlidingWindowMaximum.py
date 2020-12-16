# https://www.interviewbit.com/problems/sliding-window-maximum/

def fillNextNotSmallers(A, arr):
    stack = []
    i = 0
    while i < len(A):
        cur = A[i]
        if not stack:
            stack.append((i, cur))
        else:
            while True:
                if not stack:
                    stack.append((i, cur))
                    break
                prev = stack.pop()
                if cur >= prev[1]:
                    arr[prev[0]] = i
                else:
                    stack.append(prev)
                    stack.append((i, cur))
                    break
        i += 1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        result = [0] * (len(A) - B + 1)
        nextNotSmallers = [-1] * len(A)
        fillNextNotSmallers(A, nextNotSmallers)
        for i in range(len(result)):
            if nextNotSmallers[i] == -1:
                result[i] = A[i]
            else:
                prevJ = i
                j = i
                while True:
                    if j == -1:
                        result[i] = A[prevJ]
                        break
                    elif nextNotSmallers[j] >= i + B:
                        result[i] = A[j]
                        break
                    prevJ = j
                    j = nextNotSmallers[j]
        return result

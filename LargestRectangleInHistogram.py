# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/

def fillNextNotGreaters(A, res, leftToRight):
    stack = []
    ran = range(len(A))
    if not leftToRight:
        ran = range(len(A) - 1, -1, -1)
    for i in ran:
        elem = A[i]
        while True:
            if not stack:
                break
            prev = stack.pop()
            if elem < prev[0]:
                res[prev[1]] = i
            else:
                stack.append(prev)
                break
        stack.append((elem, i))


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if not A or len(A) == 0:
            return 0
        nextNotGreaters = [-1] * len(A)
        prevNotGreaters = [-1] * len(A)
        fillNextNotGreaters(A, nextNotGreaters, True)
        fillNextNotGreaters(A, prevNotGreaters, False)
        result = 0
        for i in range(len(A)):
            l = 0
            r = len(A) - 1
            if prevNotGreaters[i] != -1:
                l = prevNotGreaters[i] + 1
            if nextNotGreaters[i] != -1:
                r = nextNotGreaters[i] - 1
            area = (r - l + 1) * A[i]
            result = max(result, area)
        return result        

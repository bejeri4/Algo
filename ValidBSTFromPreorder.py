# https://www.interviewbit.com/problems/valid-bst-from-preorder/

def fillNextGreaters(nextGreaters, A):
    stack = []
    for i in range(len(A)):
        elem = A[i]
        while stack:
            if elem > A[stack[-1]]:
                nextGreaters[stack[-1]] = i
                stack.pop()
            else:
                break
        stack.append(i)
            

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        nextGreaters = [-1] * len(A)
        fillNextGreaters(nextGreaters, A)
        root = -math.inf
        stack = []
        for i in range(len(A)):
            elem = A[i]
            if elem < root:
                return 0
            while stack and elem > stack[-1]:
                root = stack.pop()
            stack.append(elem)
        return 1

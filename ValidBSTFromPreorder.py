# https://www.interviewbit.com/problems/valid-bst-from-preorder/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
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

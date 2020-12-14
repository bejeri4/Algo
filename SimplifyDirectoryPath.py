
# https://www.interviewbit.com/problems/simplify-directory-path/

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        ls = A.split('/')
        stack = []
        for elem in ls:
            if elem == "." or elem == "":
                continue
            elif elem == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(elem)
        result = ""
        while stack:
            result += stack.pop()[::-1] + "/"
        if result == "":
            return "/"
        return result[::-1]

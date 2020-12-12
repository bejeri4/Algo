# https://www.interviewbit.com/problems/generate-all-parentheses-ii/

def generate(k, balance, current, result):
    if k == 0:
        result.append(current)
        return
    if balance == 0:
        generate(k - 1, balance + 1, current + "(", result)
    else:
        if balance < k:
            generate(k - 1, balance + 1, current + "(", result)
        generate(k - 1, balance - 1, current + ")", result)

class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        result = []
        generate(2 * A, 0, "", result)
        return result
        

# https://www.interviewbit.com/problems/gray-code/

def generate(n, result):
    if n == 0:
        return
    if n == 1:
        result.append("0")
        result.append("1")
        return
    generate(n - 1, result)
    for i in range(len(result)):
        result[i] = "0" + result[i]
    for i in range(len(result) - 1, -1, -1):
        result.append("1" + result[i][1:])
    
    
def toDecimal(b):
    result = 0
    for i in b[::-1]:
        result = result * 2 + ord(i) - ord("0")
    return result
    
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        result = []
        generate(A, result)
        for i in range(len(result)):
            result[i] = toDecimal(result[i])
        return result

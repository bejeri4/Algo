# https://www.interviewbit.com/problems/evaluate-expression/

def isOperator(s):
    return s == "+" or s == "-" or s == "*" or s == "/"
    
def applyOperator(a, b, o):
    a = int(a)
    b = int(b)
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        return a // b

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        nums = []
        operators = []
        for elem in A:
            if isOperator(elem):
                if len(nums) > 1:
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(applyOperator(a, b, elem))
                else:
                    operators.apped(elem)
            else:
                nums.append(elem)
        while operators:
                b = nums.pop()
                a = nums.pop()
                nums.append(applyOperator(a, b, operators.pop()))
        return nums[0]

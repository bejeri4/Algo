# https://www.interviewbit.com/problems/multiply-strings/

def getProduct(A, d):
    result = []
    carry = 0
    i = len(A) - 1
    while i >= 0:
        curP = int(d) * int(A[i]) + carry
        carry = curP // 10
        result.append(str(curP)[-1])
        i -= 1
    result.append(str(carry))
    return result[::-1]
        

def addTwoDigits(a, b, carry):
    result = str(int(a) + int(b) + int(carry))
    if len(result) < 2:
        return (str(result), 0)
    else:
        return (str(result[-1]), 1)

def addProduct(arr, p, rightIndex):
    i = rightIndex
    j = len(p) - 1
    carry = 0
    while j >= 0:
        sumDigits, carry = addTwoDigits(arr[i], p[j], carry)
        arr[i] = sumDigits
        i -= 1
        j -= 1

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        arr = ["0"] * (len(A) + len(B))
        rightIndex = len(arr) - 1
        for d in B[::-1]:
            product = getProduct(A, d)
            addProduct(arr, product, rightIndex)
            rightIndex -= 1
        result = ""
        i = 0
        while i < len(arr):
            if arr[i] != "0":
                break
            i += 1
        if i == len(arr):
            return 0
        while i < len(arr):
            result += arr[i]
            i += 1
        return result

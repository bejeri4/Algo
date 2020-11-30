# https://www.interviewbit.com/problems/palindromic-binary-representation/

def toDecimal(arr):
    result = 0
    i = len(arr) - 1
    p = 1
    while i >= 0:
        result += arr[i] * p
        i -= 1
        p *= 2
    return result
        
def addOne(arr):
    i = len(arr) - 1
    while i >= 0:
        arr[i] += 1
        if arr[i] == 2:
            arr[i] = 0
        else:
            break
        i -= 1

def getIthPalindrome(i, numBits):
    arr = [0] * ((numBits + 1) // 2)
    arr[0] = 1
    j = 1
    while True:
        if j == i:
            if numBits % 2 == 0:
                arr = arr + arr[::-1]
            else:
                arr = arr + arr[:-1][::-1]
            return toDecimal(arr)
        j += 1
        addOne(arr)

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        numPalindromes = 0
        incr = 1
        numBits = 0
        while True:
            for _ in range(2):
                numPalindromes += incr
                numBits += 1
                if numPalindromes >= A:
                    localIndex = A - (numPalindromes - incr)
                    return getIthPalindrome(localIndex, numBits)
            incr *= 2
        
        

# https://www.interviewbit.com/problems/seats/

p = 10000003

class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        result = 0
        arr = list(A)
        m = getMidIndex(arr)
        l = m
        r = m
        while l >= 0 and arr[l] == "x":
            l -= 1
        while r < len(arr) and arr[r] == "x":
            r += 1
        i = l
        while i >= 0:
            if arr[i] == "x":
                result = (result + l - i) % p
                l -= 1
            i -= 1
        i = r
        while i < len(arr):
            if arr[i] == "x":
                result = (result + i - r) % p
                r += 1
            i += 1
        return result
        
            
            
def getMidIndex(arr):
    numX = 0
    for elem in arr:
        if elem == "x":
            numX += 1
    if numX > 1:
        numX = (numX + 1) / 2
    i = 0
    while True:
        if arr[i] == "x":
            numX -= 1
        if numX == 0:
            break
        i += 1
    return i
    

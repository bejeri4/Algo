# https://www.interviewbit.com/problems/window-string/

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if not A or not B or len(A) < len(B):
            return ""
        target = dict()
        for elem in B:
            if elem not in target:
                target[elem] = 0
            target[elem] += 1
        curDict = dict()
        l = 0
        r = 0
        numFound = 0
        result = ""
        while r < len(A):
            elem = A[r]
            if elem in target:
                if elem not in curDict:
                    curDict[elem] = 1
                    numFound += 1
                else:
                    if curDict[elem] < target[elem]:
                        numFound += 1
                    curDict[elem] += 1
            if numFound == len(B):
                if result == "":
                    result = A[l : r + 1]
                while True:
                    elem = A[l]
                    if elem in target:
                        cnt = curDict[elem] - 1
                        curDict[elem] -= 1
                        if r - l + 1 < len(result):
                            result = A[l : r + 1]
                        l += 1
                        if cnt < target[elem]:
                            numFound -= 1
                            while l < r and A[l] not in target:
                                l += 1
                            break
                    else:
                        l += 1
            r += 1
        return result

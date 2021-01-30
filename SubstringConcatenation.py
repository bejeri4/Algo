# https://www.interviewbit.com/problems/substring-concatenation/

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        result = []
        if not B:
            return result
        target = dict()
        for elem in B:
            if elem not in target:
                target[elem] = 0
            target[elem] += 1
        curDict = dict()
        numFound = 0
        n = len(B[0])
        i = 0
        start = i
        while i < len(A):
            word = A[i : i + n]
            if word not in curDict:
                curDict[word] = 0
            curDict[word] += 1
            if word in target and curDict[word] <= target[word]:
                numFound += 1
                i += n
            else:
                numFound = 0
                curDict.clear()
                start += 1
                i = start
            if numFound == len(B):
                result.append(start)
                numFound = 0
                curDict.clear()
                start += 1
                i = start
        return result

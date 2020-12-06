# https://www.interviewbit.com/problems/justified-text/

def numExtraSpaces(arr, maxLen):
    l = 0
    for w in arr:
        l += len(w)
    return maxLen - l

def lineFromWords(arr, maxLen):
    numSpaces = numExtraSpaces(arr, maxLen)
    if len(arr) == 1:
        arr[0] += " " * numSpaces
    else:
        w = 0
        while numSpaces > 0:
            arr[w] += " "
            w = (w + 1) % (len(arr) - 1)
            numSpaces -= 1
    return "".join(arr)


def lastLineFromWords(arr, maxLen):
    numSpaces = numExtraSpaces(arr, maxLen)
    if len(arr) == 1:
        arr[0] += " " * numSpaces
    else:
        for i in range(len(arr)):
            if numSpaces == 0:
                break
            arr[i] += " "
            numSpaces -= 1
        arr[-1] += " " * numSpaces
    return "".join(arr)

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(Self, A, B):
        if not A:
            return []
        lines = []
        i = 0
        curLine = []
        curLineLen = 0
        while i < len(A):
            if curLineLen + len(A[i]) == B:
                curLine.append(A[i])
                curLineLen += len(A[i])
            elif curLineLen + len(A[i]) + 1 <= B:
                curLine.append(A[i])
                curLineLen += len(A[i]) + 1
            else:
                lines.append(curLine)
                curLineLen = 0
                curLine = []
                continue
            i += 1
        if len(curLine) > 0:
            lines.append(curLine)
        result = []
        for wordsArr in lines[:-1]:
            result.append(lineFromWords(wordsArr, B))
        result.append(lastLineFromWords(lines[-1], B))
        return result
            
            
            

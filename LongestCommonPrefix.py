# https://www.interviewbit.com/problems/longest-common-prefix/

def setString(arr, s):
    i = 0
    while i < len(arr) and i < len(s):
        if arr[i] != s[i]:
            break
        i += 1
    return arr[:i]

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 0:
            return ""
        arr = list(A[0])
        for s in A[1:]:
            arr = setString(arr, s)
        return "".join(arr)

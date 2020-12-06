# https://www.interviewbit.com/problems/longest-palindromic-substring/

def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return  False
    return True
    
 
class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        for length in range(len(A), -1, -1):
            for i in range(len(A) - length + 1):
                s = A[i: i + length]
                if isPalindrome(s):
                    return s

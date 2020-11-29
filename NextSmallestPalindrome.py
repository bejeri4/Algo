# https://www.interviewbit.com/problems/next-smallest-palindrome/

def isPalindrome(A):
    for i in range(len(A) // 2):
        if A[i] != A[len(A) - 1 - i]:
            return False
    return True
    
def increaseByOne(A):
    arr = list(A)
    arr.reverse()
    for i in range(len(arr)):
        d = int(arr[i]) + 1
        arr[i] = str(d)[-1]
        if d < 10:
            arr.reverse()
            return "".join(arr)
    arr.append("1")
    arr.reverse()
    return "".join(arr)

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        fh = A[:len(A) // 2]
        middle = ""
        if len(A) % 2 == 1:
            middle = A[len(A) // 2]
        possibleAnswer = fh + middle + fh[::-1]
        if isPalindrome(possibleAnswer) and possibleAnswer > A:
            return possibleAnswer
        if len(A) % 2 == 1:
            fh = fh + middle
        increased = increaseByOne(fh)
        if len(A) % 2 == 1:
            if len(increased) > len(fh):
                return increased[:--1] + increased[:-1][::-1]
            else:
                return increased + increased[:-1][::-1]
        else:
            if len(increased) > len(fh):
                return increased + increased[:-1][::-1]
            else:
                return increased + increased[::-1]

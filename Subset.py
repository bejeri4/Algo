# https://www.interviewbit.com/problems/subset/

from functools import cmp_to_key

def generate(A, curIndex, result, soFar):
    if curIndex == len(A):
        result.append(soFar.copy())
        return
    generate(A, curIndex + 1, result, soFar)
    soFar.append(A[curIndex])
    generate(A, curIndex + 1, result, soFar)
    soFar.pop()

# str1 = "".join(str(e) for e in ls1)
def cmpFn(ls1, ls2):
    i = 0
    while i < len(ls1) and i < len(ls2):
        if ls1[i] < ls2[i]:
            return -1
        if ls1[i] > ls2[i]:
            return 1
        i += 1
    if len(ls1) == len(ls2):
        return 0
    if i >= len(ls1):
        return -1
    return 1

        
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        result = []
        soFar = []
        generate(A, 0, result, soFar)
        result.sort(key=cmp_to_key(cmpFn))
        return result

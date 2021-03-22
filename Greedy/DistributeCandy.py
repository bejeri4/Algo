# https://www.interviewbit.com/problems/distribute-candy/

from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        if not A or len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        arr = []
        for i in range(len(A)):
            arr.append([A[i], i])
        arr.sort(key = cmp_to_key(cmpFn))
        given = [0] * len(A)
        for i in range(len(arr)):
            index = arr[i][1]
            if index == 0:
                if A[0] <= A[1]:
                    given[0] = 1
                else:
                    given[0] = given[1] + 1
            elif index == len(A) - 1:
                if A[-1] <= A[-2]:
                    given[-1] = 1
                else:
                    given[-1] = given[-2] + 1
            else:
                if A[index] == A[index - 1] and A[index] == A[index + 1]:
                    given[index] = 1
                elif A[index] == A[index - 1]:
                    given[index] = given[index + 1] + 1
                elif A[index] == A[index + 1]:
                    given[index] = given[index - 1] + 1
                else:
                    given[index] = max(given[index -1] + 1, given[index +1] + 1)
        return sum(given)
                
def cmpFn(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return a[0] - b[0]

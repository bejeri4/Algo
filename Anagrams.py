# https://www.interviewbit.com/problems/anagrams/

from functools import cmp_to_key

def cmpFnStr(a, b):
    arr1 = a[0]
    arr2 = b[0]
    for i in range(len(arr1)):
        if i == len(arr2):
            return 1
        dif = ord(arr1[i]) - ord(arr2[i])
        if dif > 0:
            return 1
        elif dif < 0:
            return -1
        else:
            i += 1
    if len(arr1) == len(arr2):
        return 0
    return -1

def cmoFnIndex(a, b):
    return a[1] - b[1]

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        if not A:
            return []
        if len(A) == 1:
            return [[1]]
        arr = list(A)
        for i in range(len(arr)):
            arr[i] = (sorted(arr[i]), i + 1)
        arr.sort(key = cmp_to_key(cmpFnStr))
        clasters = []
        curClaster = []
        curClaster.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i][0] == arr[i - 1][0]:
                curClaster.append(arr[i])
            else:
                clasters.append(curClaster)
                curClaster = []
                curClaster.append(arr[i])
        if curClaster:
            clasters.append(curClaster)
        result = []
        for claster in clasters:
            claster.sort(key = cmp_to_key(cmoFnIndex))
            ans = []
            for elem in claster:
                ans.append(elem[1])
            result.append(ans)
        return result

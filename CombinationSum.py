# https://www.interviewbit.com/problems/combination-sum/

from functools import cmp_to_key


def generate(nums, curIndex, result, soFar, target):
    if target == 0:
        result.append(soFar.copy())
        return
    if target < 0 or curIndex >= len(nums):
        return
    soFar.append(nums[curIndex])
    generate(nums, curIndex, result, soFar, target - nums[curIndex])
    soFar.pop()
    generate(nums, curIndex + 1, result, soFar, target)
    
    
def cmpFf(ls1, ls2):
    i = 0
    while i < len(ls1) and i < len(ls2):
        if ls1[i] < ls2[i]:
            return -1
        if ls1[i] > ls2[i]:
            return -1
    if len(ls1) == len(ls2):
        return 0
    elif i >= len(ls1):
        return -1
    else:
        return 1


def removeDuplicates(A):
    st = set(A)
    A.clear()
    for elem in st:
        A.append(elem)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        removeDuplicates(A)
        A.sort()
        result = []
        soFar = []
        generate(A, 0, result, soFar, B)
        return result

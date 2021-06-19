def getNumZeros(nums):
    result = 0
    for elem in nums:
        if elem == 0:
            result += 1
    return result

def getProductWithoutZero(nums):
    p = 0
    for elem in nums:
        if elem != 0:
            if p == 0:
                p = 1
            p *= elem
    return p

def oneZeroMode(nums, p):
    result = []
    for i in range(len(nums)):
        if nums[i] == 0:
            result.append(p)
        else:
            result.append(0)
    return result

def normalMode(nums, p):
    result = []
    for i in range(len(nums)):
        result.append(int(p / nums[i]))
    return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = getNumZeros(nums)
        if numZeros == 0:
            return normalMode(nums, getProductWithoutZero(nums))
        elif numZeros == 1:
            return oneZeroMode(nums, getProductWithoutZero(nums))
        else:
            return [0] * len(nums)


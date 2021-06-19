class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        s = 0
        dct = dict()
        dct[0] = 1
        for elem in nums:
            s += elem
            if s - k in dct:
                result += dct[s - k]
            if s not in dct:
                dct[s] = 0
            dct[s] += 1
        return result

class Solution:
    def rob(self, nums: List[int]) -> int:
        robHouse = 0
        skipHouse = 0
        for elem in nums:
            skipHouse = max(robHouse, skipHouse)
            robHouse += elem
            robHouse, skipHouse = skipHouse, robHouse
        return max(robHouse, skipHouse)

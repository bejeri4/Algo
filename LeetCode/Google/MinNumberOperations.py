class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target or len(target) == 0:
            return 0
        result = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                result += target[i] - target[i - 1]
        return result

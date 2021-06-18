class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                d = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]
                result += d * h
            stack.append(i)
        return result

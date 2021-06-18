def mid(ls):
    if len(ls) % 2 == 1:
        return ls[len(ls) // 2]
    else:
        return (ls[(len(ls) - 1) // 2] +ls[len(ls) // 2]) / 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        if not nums1:
            return mid(nums2)
        if not nums2:
            return mid(nums1)
        nums1, nums2 = sorted([nums1, nums2], key = len)
        left = 0
        right = len(nums1)
        totalLen = len(nums1) + len(nums2)
        while left <= right:
            p1 = left + (right - left) // 2
            p2 = (totalLen + 1) // 2 - p1

            x1 = -math.inf
            x2 = math.inf
            if p1 - 1 >= 0:
                x1 = nums1[p1 - 1]
            if p1 < len(nums1):
                x2 = nums1[p1]

            y1 = -math.inf
            y2 = math.inf
            if p2 - 1 >= 0:
                y1 = nums2[p2 - 1]
            if p2 < len(nums2):
                y2 = nums2[p2]
                
            if x1 <= y2 and y1 <= x2:
                if totalLen % 2 == 0:
                    return (max(x1, y1) + min(x2, y2)) / 2
                else:
                    return max(x1, y1)
            elif x1 > y2:
                right = p1 - 1
            else:
                left = p1 + 1

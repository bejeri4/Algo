def swap(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp

def partition(arr, left, right):
    p = left
    while left < right:
        while left < len(arr) and arr[left] <= arr[p]:
            left += 1
        while arr[right] > arr[p]:
            right -= 1
        if left < right:
            swap(arr, left, right)
    swap(arr, p, right)
    return right

		

def select(arr, k, left, right) -> int:
	if left == right:
		return arr[left]
	p = partition(arr, left, right)
	if p == len(arr) - k:
		return arr[p]
	if p < len(arr) - k:
		return select(arr, k, p + 1, right)
	else:
		return select(arr, k, left, p - 1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return select(nums, k, 0, len(nums) - 1)
        

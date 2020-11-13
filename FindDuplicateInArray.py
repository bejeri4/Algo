# https://www.interviewbit.com/problems/find-duplicate-in-array/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        matcher = [0] * (int(math.log(len(A) + 1, 2)) + 1)
        for elem in A:
            log = int(math.log(elem, 2))
            matcher[log] += 1
        mismatchRange = -1
        for i in range(len(matcher)):
            if 2**i != matcher[i]:
                mismatchRange = i
                break
        if mismatchRange == -1:
            return -1
        delta = 2**mismatchRange
        arr = [0] * delta
        for elem in A:
            log = int(math.log(elem, 2))
            if log == mismatchRange:
                arr[(elem - delta)] += 1
        for i in range(len(arr)):
            if arr[i] != 1:
                return i + delta
        return mismatchRange

    
    
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def repeatedNumber(self, A):
#         sum = 0
#         for elem in A:
#             sum += elem
#         return int(sum - (len(A) - 1) * len(A) / 2)

# https://www.interviewbit.com/problems/maximum-consecutive-gap/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) < 2:
            return 0
        minElem = math.inf
        maxElem = -math.inf
        for elem in A:
            minElem = min(minElem, elem)
            maxElem = max(maxElem, elem)
        if maxElem == minElem:
            return 0
        gap = (maxElem - minElem) // len(A)
        buckets = [None] * len(A)
        for elem in A:
            index = (elem - minElem) // (gap + 1)
            if not buckets[index]:
                buckets[index] = [elem, elem]
            else:
                buckets[index] = [min(elem, buckets[index][0]), max(elem, buckets[index][1])]
        i = 0
        j = 1
        result = -1
        while j < len(A):
            if not buckets[j]:
                j += 1
                continue
            result = max(result, buckets[j][0] - buckets[i][1])
            i = j
            j += 1
        return result

# https://www.interviewbit.com/problems/find-duplicate-in-array/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A) - 1
        root = math.ceil(math.sqrt(n))
        buckets = [0] * root
        for elem in A:
            buckets[(elem - 1) // root] += 1
        lastBuckIndex = n // root
        badSegment = None
        for i in range(len(buckets)):
            if buckets[i] > root:
                badSegment = i
                break
        if badSegment == None:
            badSegment = lastBuckIndex
        badBucket = [0] * root
        for elem in A:
            index = (elem - 1) // root
            if index == badSegment:
                localIndex = elem % root
                badBucket[localIndex] += 1
                if badBucket[localIndex] > 1:
                    return elem
        return -1

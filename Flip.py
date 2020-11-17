# https://www.interviewbit.com/problems/flip/

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        arr = [0] * len(A)
        cnt = 0
        maxIndex = -1
        maxCnt = -1
        for i in range(len(A)):
            if A[i] == "0":
                cnt += 1
            else:
                cnt -= 1
            if cnt > maxCnt:
                maxCnt = cnt
                maxIndex = i
            arr[i] = cnt
            cnt = max(cnt, 0)
        if maxIndex == -1:
            return []
        start = maxIndex
        end = maxIndex
        for i in range(maxIndex, -1, -1):
            if arr[i] == -1:
                break
            start -= 1
        return [start + 2, end + 1]

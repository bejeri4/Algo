# https://www.interviewbit.com/problems/meeting-rooms/

from functools import cmp_to_key

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A or len(A) == 0:
            return 0
        start = A.copy()
        end = A.copy()
        start.sort(key = cmp_to_key(cmpStart))
        end.sort(key = cmp_to_key(cmpEnd))
        i = 0
        j = 0
        result = 0
        curMeetings = 0
        while i < len(start):
            while True:
                if start[i][0] < end[j][1]:
                    break
                j += 1
                curMeetings -= 1
            curMeetings += 1
            result = max(result, curMeetings)
            i += 1
        return result
        
        
def cmpStart(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return a[0] - b[0]


def cmpEnd(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return a[1] - b[1]

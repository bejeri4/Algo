# https://www.interviewbit.com/problems/3-sum-zero/

class Triple:
    def __init__(self, ls):
        self.ls = ls
        self.ls.sort()

    def __hash__(self):
        return sum(self.ls)
        
    def __eq__(self, other):
        return self.ls[0] == other.ls[0] and self.ls[1] == other.ls[1] and self.ls[2] == other.ls[2]


def extendForIndex(arr, index, resultSet):
    i = 0
    j = len(arr) - 1
    while i < j:
        if i == index:
            i += 1
        elif j == index:
            j -= 1
        else:
            ls = [arr[i], arr[j], arr[index]]
            s = sum(ls)
            if s > 0:
                j -= 1
            elif s < 0:
                i += 1
            else:
                resultSet.add(Triple(ls))
                i += 1


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        resultSet = set()
        A.sort()
        for i in range(len(A)):
            extendForIndex(A, i, resultSet)
        result = []
        for elem in resultSet:
            result.append(elem.ls)
        return result
        
        

# https://www.interviewbit.com/problems/4-sum/

from functools import cmp_to_key

p = 7

class Ans:
    def __init__(self, ls):
        self.ls = ls
        self.ls.sort()
        
    def __eq__(self, other):
        return self.ls[0] == other.ls[0] and self.ls[1] == other.ls[1] and self.ls[2] == other.ls[2] and self.ls[3] == other.ls[3]

    def __hash__(self):
        result = 0
        power = 0
        for elem in self.ls:
            pow(p, power)
            result += power * elem
            power += 1
        return result

def cmpFn(a, b):
    return a[0] - b[0]
    
def cmpRes(a, b):
    if a[0] - b[0] != 0:
        return a[0] - b[0]
    if a[1] - b[1] != 0:
        return a[1] - b[1]
    if a[2] - b[2] != 0:
        return a[2] - b[2]
    return a[3] - b[3]

def areDifferent(ls):
    st = set(ls)
    return len(st) == 4
    

def updateRes(result, ls1, ls2, A):
    for i in ls1:
        for j in ls2:
            l = [i[0], i[1], j[0], j[1]]
            if areDifferent(l):
                result.add(Ans([ A[i[0]], A[i[1]], A[j[0]], A[j[1]] ]))
    
        
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        dct = dict()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                s = A[i] + A[j]
                if s not in dct:
                    dct[s] = []
                dct[s].append([i, j])
        st = set()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                s = A[i] + A[j]
                target = B - s
                if target in dct:
                    updateRes(st, dct[target], [[i, j]], A)
        result = []
        for elem in st:
            result.append(elem.ls)
        result.sort(key = cmp_to_key(cmpRes))
        return result







       
       
       

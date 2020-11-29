# https://www.interviewbit.com/problems/sorted-permutation-rank/

p = 1000003

def indexOfSymbol(arr, symbol):
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == symbol:
            arr.pop(mid)
            return mid
        elif symbol < arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return -1
    

def fillFactorials(facts):
    for i in range(2, len(facts)):
        facts[i] = (facts[i - 1] * i) % p

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        result = 0
        arr = sorted(A)
        facts = [1] * len(A)
        fillFactorials(facts)
        for symbol in A:
            index = indexOfSymbol(arr, symbol)
            length = len(arr)
            result += (index * facts[length]) % p
            result %= p
        return result + 1

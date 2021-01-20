# https://www.interviewbit.com/problems/distinct-numbers-in-window/

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
	    if B == 0:
	        return [0] * (len(A) - B + 1)
	    result = []
	    dct = dict()
	    left = 0
	    right = 0
	    numDistinct = 0
	    while right < len(A):
	        if right - left == B:
	            result.append(numDistinct)
	            elem = A[left]
	            if dct[elem] == 1:
	                del dct[elem]
	                numDistinct -= 1
	            else:
	                dct[elem] = dct[elem] - 1
	            left += 1
            else:
                elem = A[right]
	            if elem in dct:
	                dct[elem] += 1
	            else:
	                dct[elem] = 1
	                numDistinct += 1
	            right += 1
	    result.append(numDistinct)
	    return result

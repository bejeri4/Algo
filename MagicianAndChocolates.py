import heapq

p = 1000000007

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
	    result = 0
	    ls = []
	    for elem in B:
    	    heapq.heappush(ls, (1 / elem, elem))
	    while A > 0 and ls:
	        elem = heapq.heappop(ls)[1]
	        result += elem
	        result %= p
	        elem //= 2
	        if elem != 0:
    	        heapq.heappush(ls, (1 / elem, elem))
	        A -= 1
	    return result
	        

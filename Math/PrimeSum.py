# https://www.interviewbit.com/problems/prime-sum/

def getPrimes(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    for i in range(2, n + 1):
        if not arr[i]:
            continue
        arr[i] = True
        j = i + i
        while j < n + 1:
            arr[j] = False
            j += i
    result = []
    for i in range(len(arr)):
        if arr[i]:
            result.append(i)
    return result


class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
	    primes = getPrimes(A)
	    i = 0
	    j = len(primes) - 1
	    while True:
	        s = primes[i] + primes[j]
	        if s == A:
	            return [primes[i], primes[j]]
	        elif s < A:
	            i += 1
	        else:
	            j -= 1

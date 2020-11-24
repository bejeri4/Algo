# https://www.interviewbit.com/problems/prime-numbers/

class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        sieve = [1] * (A + 1)
        sieve[0] = 0
        sieve[1] = 0
        i = 2
        while i <= A:
            if sieve[i] == 1:
                j = i + i
                while j <= A:
                    sieve[j] = 0
                    j += i
            i += 1
        result = []
        for i in range(2, A + 1):
            if sieve[i] == 1:
                result.append(i)
        return result

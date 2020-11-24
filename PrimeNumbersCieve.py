class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        cieve = [1] * (A + 1)
        cieve[0] = 0
        cieve[1] = 0
        i = 2
        while i <= A:
            if cieve[i] == 1:
                j = i + i
                while j <= A:
                    cieve[j] = 0
                    j += i
            i += 1
        result = []
        for i in range(2, A + 1):
            if cieve[i] == 1:
                result.append(i)
        return result

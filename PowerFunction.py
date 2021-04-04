# https://www.interviewbit.com/problems/implement-power-function/

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        result = 1
        while n != 0:
            if n % 2 == 1:
                result = (result * x) % d
            x = (x * x) % d
            n //= 2
        return result

    
    
    
def power(x, n, d):
    if n == 0:
        return 1
    tmp = power(x, n // 2, d)
    result = (tmp * tmp) % d
    if n % 2 == 1:
        result = (result * x) % d
    return result

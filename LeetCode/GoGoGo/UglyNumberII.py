class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [None] * n
        ugly[0] = 1
        p2 = 0
        p3 = 0
        p5 = 0
        index = 1
        num2 = 2
        num3 = 3
        num5 = 5
        for i in range(1, n):
            num = min(num2, num3, num5)
            ugly[i] = num
            if num2 == num:
                p2 += 1
                num2 = ugly[p2] * 2
            if num3 == num:
                p3 += 1
                num3 = ugly[p3] * 3
            if num5 == num:
                p5 += 1
                num5 = ugly[p5] * 5
        return ugly[-1]

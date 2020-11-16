# https://www.interviewbit.com/problems/hotel-bookings-possible/

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()
        guests = 0
        oldestNotYetLeftIndex = 0
        for curDay in arrive:
            guests += 1
            while oldestNotYetLeftIndex < len(depart) and depart[oldestNotYetLeftIndex] <= curDay:
                guests -= 1
                oldestNotYetLeftIndex += 1
            if guests > K:
                return 0
        return 1

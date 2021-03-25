# https://www.interviewbit.com/problems/gas-station/

def canTravel(gas, cost):
    return sum(gas) >= sum(cost)
    
    
def minStart(gas, cost):
    start = 0
    curStation = 0
    curGasAmount = 0
    while curStation < len(gas):
        curGasAmount += gas[curStation]
        curGasAmount -= cost[curStation]
        if curGasAmount < 0:
            curGasAmount = 0
            start = curStation + 1
        curStation += 1
    return start
    

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        if not canTravel(A, B):
            return -1
        return minStart(A, B)

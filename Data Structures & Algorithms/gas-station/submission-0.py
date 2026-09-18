class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        t = 0
        r = 0
        if sum(gas)<sum(cost):
            return -1 
        for i in range(len(gas)):
            t+=(gas[i]-cost[i])
            if t<0:
                t=0
                r=i+1 
        return r



        
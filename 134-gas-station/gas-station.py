class Solution(object):
    def canCompleteCircuit(self, gas, cost): 
        if sum(gas) < sum(cost):
            return -1
        car_fuel,index=0,0
        for i in range(len(gas)):
            car_fuel+=gas[i]-cost[i]
            if car_fuel<0:
                index=i+1
                car_fuel=0
        return index
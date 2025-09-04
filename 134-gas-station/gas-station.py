class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas=sum(gas)
        total_cost= sum(cost)
        if total_gas < total_cost:
            return -1
        else:
            car_fuel,index=0,0
            for i in range(len(gas)):
                car_fuel+=gas[i]-cost[i]
                if car_fuel<0:
                    index=i+1
                    car_fuel=0
        return index
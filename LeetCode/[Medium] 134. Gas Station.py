from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # BRUTE FORCE - TIME LIMIT EXCEED
        # num = len(gas)
        # current_gas = 0
        # for i in range(num):
        #     current_station_index = i
        #     j = 0
        #     while j < num:
        #         current_gas += gas[current_station_index]
        #         if current_gas < cost[current_station_index]:
        #             break
        #         else:
        #             current_gas -= cost[current_station_index]
        #             current_station_index = (current_station_index + 1) % num
        #             j += 1
        #     if j == num:
        #         return i
        #     current_gas = 0
        # return -1

        # MY SOLUTION
        if sum(gas) < sum(cost):
            return -1
        start = fuel = 0
        for i in range(len(gas)):
            if fuel + gas[i] < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

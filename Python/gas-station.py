# Time:  O(n)
# Space: O(1)

# 134
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.
#


# Ituition: if sum(gas) >= sum(cost), we must be able to travel the circle.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        start, current_sum = 0, 0
        for i in range(len(gas)):
            current_sum += gas[i] - cost[i]
            if current_sum < 0:
                start = i + 1
                current_sum = 0
        return start


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1, 2, 3], [3, 2, 1])) # 1
    print(Solution().canCompleteCircuit([1, 2, 3], [2, 2, 2])) # 1
    print(Solution().canCompleteCircuit([1, 2, 3], [1, 2, 3])) # 0
    print(Solution().canCompleteCircuit([1, 2, 3], [1, 2, 4])) # -1

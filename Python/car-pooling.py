# Time:  O(nlogn)
# Space: O(n)

# 1094
# You are driving a vehicle that has capacity empty seats initially available for passengers.  
# The vehicle only drives east (ie. it cannot turn around and drive west.)

# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains 
# information about the i-th trip: the number of passengers that must be picked up, and the locations 
# to pick them up and drop them off.  The locations are given as the number of kilometers due east 
# from your vehicle's initial location.

# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        line = [x for num, start, end in trips for x in [[start, num], [end, -num]]]
        line.sort()
        for _, num in line:
            capacity -= num
            if capacity < 0:
                return False
        return True

print(Solution().carPooling([[2,1,5],[3,3,7]], 4)) # False
print(Solution().carPooling([[2,1,5],[3,3,7]], 5)) # True
print(Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11)) # True

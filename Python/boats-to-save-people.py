# Time:  O(nlogn)
# Space: O(n)

# The i-th person has weight people[i],
# and each boat can carry a maximum weight of limit.
#
# Each boat carries at most 2 people at the same time,
# provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.
# (It is guaranteed each person can be carried by a boat.)
#
# Example 1:
#
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:
#
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:
#
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# Note:
# - 1 <= people.length <= 50000
# - 1 <= people[i] <= limit <= 30000

class Solution(object):
    # two pointer / greedy
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        result = 0
        left, right = 0, len(people)-1
        while left <= right:
            result += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return result

    def numRescueBoats_bisect(self, people, limit):
        # time: n*logn
        import bisect
        N = len(people)
        people.sort(reverse=True)
        l, r = (N + 1) // 2, N

        def can(m):
            boats = [limit - x for x in people[:m]]
            for x in reversed(people[m:]):
                i = bisect.bisect_left(boats, x)
                if i >= len(boats):
                    return False
                else:
                    boats[i] = 0 # maybe a bug, boats is no longer sorted after this. Doing sort here will TLE.

            return True

        while l < r:
            m = l + (r - l) // 2
            if can(m):
                r = m
            else:
                l = m + 1
        return l
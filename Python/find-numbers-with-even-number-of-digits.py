# Time:  O(nlog(logm)), n the length of nums, m is the max value of nums
# Space: O(logm)

# 1295 weekly contest 168 12/21/2019

# Given an array nums of integers, return how many of them contain an even number of digits.
# 1 <= nums[i] <= 10^5

import bisect


class Solution(object):
    def __init__(self):
        M = 10**5
        self.__lookup = [0]
        i = 10
        while i < M:
            self.__lookup.append(i)
            i *= 10
        self.__lookup.append(i)

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_count(n):
            return bisect.bisect_right(self.__lookup, n)

        return sum(digit_count(n) % 2 == 0 for n in nums)
    

# Time:  O(nlogm), n the length of nums, m is the max value of nums
# Space: O(logm)
class Solution2(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_count(n):
            result = 0
            while n:
                n //= 10
                result += 1
            return result

        return sum(digit_count(n) % 2 == 0 for n in nums)


# Time:  O(nlogm), n the length of nums, m is the max value of nums
# Space: O(logm)
class Solution3(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(len(str(n)) % 2 == 0 for n in nums)

print(Solution().findNumbers([555,901,482,1771])) # 1
# Time:  O(n*log(sum(nums)), n is # of integers in input array
# Space: O(1)

# 1250
# Given an array nums of positive integers. Your task is to select some subset of nums,
# multiply each element by an integer and add all these numbers. The array is said to be good 
# if you can obtain a sum of 1 from the array by any possible subset and multiplicand.
#
# Return True if the array is good otherwise return False.


# SOLUTION: Bézout's identity also used in LC 365 water-and-jug-problem.py
#
# 裴蜀定理：对于a1,a2,a3,... an 的 n 个数， 一定存在 a1 * n1 + a2 * n2 + a3 * n3 + ... + an * nn = d，
# 其中 n1,n2,n3...nn 是正整数， d 为 a1,a2,a3,... an 的 n 个数的最大公约数。
#
# 算法就是 check 存不存在一个子数组，其最大公约数为 1。而这个复杂度仍然很高， 我们仍然需要枚举所有的子数组。
# 实际上我们不需要， 因为如果数组 A 是数组 B 的子集的话，那么 A 的最大公约数是 1， B一定也是 1.
# 因此我们只需要求出整体的最大公约数即可。


class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        # Bézout's identity
        result = nums[0]
        for num in nums:
            result = gcd(result, num)
            if result == 1:
                break
        return result == 1

print(Solution().isGoodArray([12, 5, 7, 23])) # True 5*3 + 7*(-2) = 1
print(Solution().isGoodArray([29, 6, 10])) # True 29*1 + 6*(-3) + 10*(-1) = 1
print(Solution().isGoodArray([3, 6])) # False
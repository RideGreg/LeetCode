# Time:  O(n)
# Space: O(1)

# 229
# Given an integer array of size n,
# find all elements that appear more than [n/3] times. There is no guarantee that
# the majority element must exist in the array.

# The algorithm should run in linear time and in O(1) space.

import collections

class Solution(object):
    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums): # USE THIS: general for any k of more than [n/k] times
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k, n, cnts = 3, len(nums), collections.defaultdict(int)

        # Linear scan and count input, get the candidates of majority elements saved in 'cnts'.
        # At most there is k-1 numbers can appear [n/k] times, so whenever we see
        # k different numbers, we can throw away a number. Minority will be throw away.
        # Since k is constant, this takes O(1) space.
        for i in nums:
            cnts[i] += 1
            # Detecting k items in cnts, at least one of them must have exactly
            # one in it. We will discard those k items by one for each.
            # This action keeps the same mojority numbers in the remaining numbers.
            # Because if x / n  > 1 / k is true, then (x - 1) / (n - k) > 1 / k is also true.
            if len(cnts) == k:
                keys_to_delete = []
                for x in cnts:
                    cnts[x] -= 1
                    if cnts[x] == 0:
                        keys_to_delete.append(x)
                for x in keys_to_delete:
                    del cnts[x]

        # Resets cnts for the following counting.
        for x in cnts:
            cnts[x] = 0

        # Counts the occurrence of each candidate integer.
        for x in nums:
            if x in cnts:
                cnts[x] += 1

        # Selects the integer which occurs > [n / k] times.
        return [x for x in cnts if cnts[x] > n // k]


    # Same Boyer-Moore Voting Algorithm, for [n/3] case only
    def majorityElement3(self, nums):
        a = b = None        # 设定1号众数和2号众数
        count_a = count_b = 0
        for i in nums:
            # 投票过程. 频数统计的优先顺序要大于频数为0的判断
            if a == i:  # 如果是候选者a or b，票数++
                count_a += 1
            elif b == i:
                count_b += 1
            # 如果不是候选者
            elif count_a == 0: # 如没有候选者，用此数作为候选者
                a = i
                count_a = 1
            elif count_b == 0:
                b = i
                count_b = 1
            else: # 不是已知候选者，票数--
                count_a -= 1
                count_b -= 1

        count_a, count_b = 0, 0  # 重置计数器
        for j in nums:  # 再检验
            if j == a:
                count_a += 1
            elif j == b:
                count_b += 1
        return [k for k, c in [(a, count_a), (b, count_b)] if c > len(nums)//3]


    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [k for k, c in collections.Counter(nums).items() if c > len(nums) // 3]

print(Solution().majorityElement([1,1,1,3,3,2,2,2])) # [1,2]
print(Solution().majorityElement([3,2,3])) # [3]
print(Solution().majorityElement([1,2,3,4,5])) # []
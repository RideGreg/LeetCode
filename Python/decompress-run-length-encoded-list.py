# Time:  O(n)
# Space: O(1)

# 1313 biweekly contest 17 1/11/2020

# We are given a list nums of integers representing a list compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate
# all the sublists from left to right to generate the decompressed list.
#
# Return the decompressed list.

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # wrong [[2], [4, 4, 4]]
        #return [[nums[i+1]] * nums[i] for i in range(0, len(nums), 2)]
        ans = []
        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i + 1]
            ans.extend([b] * a)
        return ans

        # OR
        return [nums[i + 1] for i in range(0, len(nums), 2) for _ in range(nums[i])]

print(Solution().decompressRLElist([1,2,3,4])) # [2,4,4,4]
print(Solution().decompressRLElist([1,1,2,3])) # [1,3,3]

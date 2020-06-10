# Time:  O(n)
# Space: O(n)
# 128
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#

import collections

class Solution:
    # @param num, a list of integer
    # @return an integer

    # only maintain the length for numbers at the two ends of consecutive sequence
    def longestConsecutive(self, num):
        ans, lengths = 0, collections.defaultdict(int)
        for n in num:
            if lengths[n] != 0: continue # skip duplicate

            left, right = lengths[n-1], lengths[n+1]
            cur = 1 + left + right
            lengths[n - left] = lengths[n + right] = lengths[n] = cur # KENG: necessary to set lengths[n] to skip next time
                                                                      # otherwise [4,5,7,6,6] returns 7
            ans = max(ans, cur)
        return ans

    def longestConsecutive_wrong(self, nums): # [0,1,-1] => 2 wrong
        begin, end, ans = collections.defaultdict(int), collections.defaultdict(int), 0
        for n in nums:
            begin[n] = 1 + begin[n+1]
            end[n] = 1 + end[n-1]
            ans = max(ans, 1 + begin[n+1] + end[n-1])
        return ans

if __name__ == "__main__":
    print(Solution().longestConsecutive([0, 0, 1, 2, -1])) # 4
    print(Solution().longestConsecutive([4, 5, 7, 6, 6])) # 4
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
    print(Solution().longestConsecutive([100, 4, 2, 200, 101, 2, 1, 3, 7, 6, 5])) # 7
    print(Solution().longestConsecutive([100])) # 1
    print(Solution().longestConsecutive([100, 4])) # 1
    print(Solution().longestConsecutive([])) # 0

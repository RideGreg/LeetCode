# Time:  O(T * S^T)
# Space: O(T * S^T)

# 691
# We are given N different types of stickers. Each sticker has a lowercase English word on it.
#
# You would like to spell out the given target string by cutting individual letters
# from your collection of stickers and rearranging them.
#
# You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
#
# What is the minimum number of stickers that you need to spell out the target?
# If the task is impossible, return -1.
#
# Example 1:
#
# Input:
# ["with", "example", "science"], "thehat"
#
# Output:
# 3
#
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
#
# Example 2:
#
# Input:
# ["notice", "possible"], "basicbasic"
#
# Output:
# -1
#
# Explanation:
# We can't form the target "basicbasic" from cutting letters from the given stickers.
#
# Note:
# - stickers has length in the range [1, 50].
# - stickers consists of lowercase English words (without apostrophes).
# - target has length in the range [1, 15], and consists of lowercase English letters.
# - In all test cases, all words were chosen randomly from the 1000 most common US English words,
#   and the target was chosen as a concatenation of two random words.
# - The time limit may be more challenging than usual.
#   It is expected that a 50 sticker test case can be solved within 35ms on average.

import collections


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        # dp 记录target字的所有子序列被覆盖所需最少的sticker数目
        # similar to backpack dp, gradually go up until processing the target string
        dp = [0] + [-1] * ((1 <<  len(target)) - 1)
        tcnt = collections.Counter(target)

        # 每个sticker能cover到的target字中的字符，过滤掉sticker with less coverage
        scnts = [collections.Counter(s) & tcnt for s in stickers]
        for x in range(len(scnts) - 1, -1, -1):
            if any(scnts[x] & scnts[y] == scnts[x] for y in range(len(scnts)) if x != y):
                scnts.pop(x)

        # 从最短子序列逐步转移到长子序列
        for status in range(1 << len(target)):
            if dp[status] < 0: continue
            for scnt in scnts:
                nstatus = status
                cnt = collections.Counter(scnt)  # copy scnt to avoid referencing to the same memory
                for i, c in enumerate(target):
                    if cnt[c] > 0 and status & (1 << i) == 0: # prev status not spell this position in 'target' string
                        nstatus |= (1 << i)
                        cnt[c] -= 1
                if dp[nstatus] == -1 or dp[nstatus] > dp[status] + 1:
                    dp[nstatus] = dp[status] + 1
        return dp[-1]

    def minStickers2(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        def minStickersHelper(target, dp):
            if "".join(target) in dp:
                return dp["".join(target)]
            target_count = collections.Counter(target)
            result = float("inf")
            for sticker_count in sticker_counts:
                if sticker_count[target[0]] == 0:
                    continue
                new_target = []
                for k in target_count.keys():
                    if target_count[k] > sticker_count[k]:
                       new_target += [k]*(target_count[k] - sticker_count[k])
                if len(new_target) != len(target):
                    num = minStickersHelper(new_target, dp)
                    if num != -1:
                        result = min(result, 1+num)
            dp["".join(target)] = -1 if result == float("inf") else result
            return dp["".join(target)]

        sticker_counts = map(collections.Counter, stickers)
        dp = { "":0 }
        return minStickersHelper(target, dp)


print(Solution().minStickers(["with", "example", "science"], "thehat")) # 3
# dp[0] = 0, dp[3]=1, dp[20]=1, dp[23]=2, dp[43]=2, dp[63]=3
# ''         'th----' '--e-a-'  'the-a-'  'th-h-t'  'thehat'

print(Solution().minStickers(["notice", "possible"], "basicbasic")) # -1

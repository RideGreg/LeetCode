# Time:  O(1)
# Space: O(1)

# 458
# There are 1000 buckets, one and only one of them contains poison,
# the rest are filled with water. They all look the same.
# If a pig drinks that poison it will die within 15 minutes.
# What is the minimum amount of pigs you need to figure out
# which bucket contains the poison within one hour.
#
# Answer this question, and write an algorithm for the follow-up general case.
#
# Follow-up:
#
# If there are n buckets and a pig drinking poison will die within m minutes,
# how many pigs (x) you need to figure out the "poison" bucket within p minutes?
# There is exact one bucket with poison.


# 不要去关注细节到底应该怎么喂水。先思考在考察哪方面的问题，数组、链表、二叉树还是数学？本题考察数学中的 进制 问题。
# 从简单情况开始，假设1只小猪可以喝2次水，能够表示3个状态：喝完第1次死，喝完第2次死，2次后仍然存活。可辨别3^1 = 3桶水。
#
# 假设2只小猪可以喝2次水，每只代表3个状态。第1只猪按行喝水，第2只猪按列喝水，根据交叉死亡时间可辨别3^2 = 9桶水。
# 0 1 2
# 3 4 5
# 6 7 8

# 假设3只小猪可以喝1次水，每只代表2个状态。每只只猪按列喝水，根据交叉死亡时间可辨别2^3 = 8桶水。
# pig1 pig2 pig3
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1

# 所以可以辨别的水桶数目 <= states ^ (#ofpigs)

import math


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(states))

print(Solution().poorPigs(100, 15, 60)) # 3
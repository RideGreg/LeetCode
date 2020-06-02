# Time:  O(a^2 + n), a is the number of ages,
#                    n is the number of people
# Space: O(a)

# 825
# Some people will make friend requests.
# The list of their ages is given and ages[i] is the age of the ith person.
#
# Person A will NOT friend request person B (B != A)
# if any of the following conditions are true:
#
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.
#
# Note that if A requests B, B does not necessarily request A.
# Also, people will not friend request themselves.
#
# How many total friend requests are made?
#
# Example 1:
#
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# Example 2:
#
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# Example 3:
#
# Input: [20,30,100,110,120]
# Output:
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
#
# Notes:
# - 1 <= ages.length <= 20000.
# - 1 <= ages[i] <= 120.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

import collections


class Solution(object):
    # answer depends on ages not people, so we should COMPRESS data first by merge people w/ same age.
    # otherwise LTE with repeating calculation of people w/ same ages.
    def numFriendRequests(self, ages): # USE THIS
        """
        :type ages: List[int]
        :rtype: int
        """
        def request(a, b):
            return 0.5*a+7 < b <= a

        c = collections.Counter(ages)
        ans = 0
        for a in c:
            for b in c:
                if request(a, b):
                    ans += c[a]*c[b] if a != b else c[a]*(c[a]-1)
        return ans

    def numFriendRequests_ming(self, ages): # similar to the above, but separate a-a and a-b, more clearly
        cnt = collections.Counter(ages)
        ans = sum(cnt[k]*(cnt[k]-1) for k in cnt if k > 14)

        # sort so only consider one way
        unique = sorted(cnt)
        for i in range(len(unique)):
            for j in range(i):
                ans += int(unique[j] > (0.5*unique[i]+7)) * cnt[unique[i]] * cnt[unique[j]]
        return ans

    def numFriendRequests_bookshadow(self, ages): # 不用看了
        '''
        观察题设条件 1 <= ages[i] <= 120，年龄的范围很小, 统计每一个年龄的人数
        遍历每个人，统计符合其年龄条件约束的人数之和
        '''
        cnt = collections.Counter(ages)
        ans = 0
        for age in ages:
            cnt[age] -= 1
            left, right = age / 2 + 8, age
            ans += sum(cnt[age] for age in range(left, right + 1))
            cnt[age] += 1
        return ans

print(Solution().numFriendRequests([69, 24, 85, 8, 85])) # 4
# Time:  O(s1 * min(s2, n1))
# Space: O(s2)

# 466
# Define S = [s,n] as the string S which consists of n connected strings s.
# For example, ["abc", 3] ="abcabcabc".
#
# On the other hand, we define that string s1 can be obtained from string s2
# if we can remove some characters from s2 such that it becomes s1.
# For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.
#
# You are given two non-empty strings s1 and s2 (each at most 100 characters long)
# and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2,
# where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.
#
# Example:
#
# Input:
# s1="acb", n1=4
# s2="ab", n2=2
#
# Return:
# 2

class Solution(object):
    # 利用贪心算法计算s1与s2对应字符的匹配位置，由于s1与s2的循环匹配呈现周期性规律，因此通过辅助数组dp进行记录
    # 记l1, l2为s1, s2的长度；x1, x2为拓展后的s1*n1, s2*n2的字符下标
    #
    # 令y1, y2 = x1 % l1, x2 % l2
    # 当s1[y1] == s2[y2]时：
    #   若dp[y1,y2]不存在，则令dp[y1,y2] = x1, x2
    #   否则，记px1, px2 = dp[y1,y2]，循环节为s1[px1 ... x1], s2[px2 ... x2]
    #
    # 用完n1个s1，看拓展后的s2的下标能前进到哪里
    def getMaxRepetitions(self, s1, n1, s2, n2): # USE THIS
        if not set(s2) <= set(s1):
            return 0

        dp = {}
        l1, l2 = len(s1), len(s2)
        x1 = x2 = 0
        while x1 < l1 * n1:
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
            if x1 >= l1 * n1:
                break
            y1, y2 = x1 % l1, x2 % l2
            if (y1, y2) not in dp:
                dp[y1, y2] = (x1, x2)
            else:
                px1, px2 = dp[y1, y2]
                loop = (l1 * n1 - px1) // (x1 - px1)
                x1 = px1 + loop * (x1 - px1)
                x2 = px2 + loop * (x2 - px2)
            if x1 < l1 * n1:
                x1 += 1
                x2 += 1

        # x2下标前进到最后，优于计算prefix_count + pattern_count + suffix_count
        return x2 // (n2 * l2)


    # https://leetcode.com/problems/count-the-repetitions/solution/
    def getMaxRepetitions_kamyu(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        repeat_count = [0] * (len(s2)+1) # count of repititions till the present s1 block
        lookup = {} # each index in s2 uses how many s1
        j, count = 0, 0 # j is index in s2, count is for s2
        for k in range(1, n1+1):
            # iterate s1, see what is j and count for s2
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j = (j + 1) % len(s2)
                    count += (j == 0)

            if j in lookup:   # cyclic
                i = lookup[j]
                prefix_count = repeat_count[i]
                pattern_count = (count - repeat_count[i]) * ((n1 - i) // (k - i))
                suffix_count = repeat_count[i + (n1 - i) % (k - i)] - repeat_count[i]
                return (prefix_count + pattern_count + suffix_count) / n2
            lookup[j] = k
            repeat_count[k] = count

        return repeat_count[n1] / n2  # not cyclic iff n1 <= s2


print(Solution().getMaxRepetitions('acb', 4, 'd', 1)) # 0
print(Solution().getMaxRepetitions('acb', 4, 'ab', 2)) # 2
print(Solution().getMaxRepetitions('acb', 4, 'aba', 2)) # 1
print(Solution().getMaxRepetitions('acbacb', 4, 'ab', 2)) # 4

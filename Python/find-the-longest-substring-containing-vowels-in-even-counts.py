# Time:  O(n)
# Space: O(1)

# 1371
# Given the string s, return the size of the longest substring containing each vowel an even number of times.
# That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

# from leetcode-cn.com 前缀和 + 状态压缩
# 暴力方法：枚举所有子串，遍历子串中的所有字符，统计元音字母出现的个数 O(n^3)

# 优化：如何在不重复遍历子串的前提下，快速求出区间里元音字母出现的次数呢？答案就是对每个元音字母维护
# 一个前缀和，对于一个区间，我们可以用两个前缀和的差值，得到这个字母的出现次数。

# 继续优化：前缀和优化了统计子串的时间复杂度，枚举所有子串的复杂度仍需O(n^2)。如何避免枚举所有子串？
# 有经验的读者马上就想到利用哈希表来优化查找的复杂度。可是本题不像1248 count-number-of-nice-subarrays
# 明确知道两个前缀的差值是恒定的。本题需要利用奇偶性，从维护元音出现的次数改作维护元音字母出现次数的奇偶性。

# 继续优化：如果直接以每个元音字母出现次数的奇偶性为哈希表中的键，键需要记录5个元音字母，假如题目稍作修改
# 扩大了字符集，维护起来会很吃力。考虑到出现次数的奇偶性无非就两个值，0代表出现偶数次，1代表奇数次，
# 我们将其压缩到一个二进制数中，仅用一个bit就代表了1个元音字母出现的奇偶性。5个元音字母可用00000->11111表示。

class Solution(object):
    def findTheLongestSubstring(self, s): # USE THIS
        """
        :type s: str
        :rtype: int
        """
        vowels, state = 'aeiou', 0
        first, last = {0: -1}, {0: -1}
        for i, c in enumerate(s):
            if c in vowels:
                k = vowels.index(c)
                mask = 1 << k
                state ^= mask
            if state not in first:
                first[state] = i
            last[state] = i
        return max(last[k] - first[k] for k in first)

    def findTheLongestSubstring_kamyu(self, s): # prefer not to use list to store states, many empty slots
        vowels, state, result = "aeiou", 0, 0
        first = [None]*(2**len(vowels))
        first[0] = -1
        for i, c in enumerate(s):
            index = vowels.find(c) # return -1 if not find, better than .index(c) which sends ValueError: substring not found
                                   # but find method ony exists for string not list.
            state ^= (1 << index) if index >= 0 else 0
            if first[state] is None:
                first[state] = i
            result = max(result, i-first[state])
        return result

    def findTheLongestSubstring_wrong(self, s: str) -> int:
        import collections
        first, counts = {}, collections.defaultdict(int)
        ans = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                if c not in first:
                    first[c] = i
                counts[c] += 1
            left = -1
            for k, v in counts.items():
                if v & 1:
                    left = max(first[k], left) # wrong, all vowels before 'left' are deducted
            ans = max(ans, i-left)
        return ans

# wrong solution 6 'rauaee': based on counts {'u': 3, 'a': 3, 'e': 2} and set left as 2 = max(first['u'], first['a'])
# which removes 1 'a' but also 2 'u'
print(Solution().findTheLongestSubstring('uuarauaee')) # 5 'uuara'

print(Solution().findTheLongestSubstring("eleetminicoworoep")) # 13 "leetminicowor"

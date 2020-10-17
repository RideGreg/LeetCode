# Time:  O(n)
# Space: O(1)

# 3 最长无重复子串
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution:
    # USE THIS: HashMap stores # of occurrence, good for problem appearing up to k times
    def lengthOfLongestSubstring(self, s):
        import collections
        ans, start, ht = 0, 0, collections.defaultdict(int)
        for end, v in enumerate(s):
            ht[v] += 1

            # freq is larger than required, shrink window
            while ht[v] > 1:
                ht[s[start]] -= 1
                start += 1
            ans = max(ans, end-start+1)
        return ans


    # this solution is easy to make mistake, use Hash Table to store the last position of a char
    # rather than to store the times a char appears
    def lengthOfLongestSubstring2(self, s: str) -> int:
        start, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > start:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                start = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-start)
        return res



print(Solution().lengthOfLongestSubstring3("abcabcbb")) # 3

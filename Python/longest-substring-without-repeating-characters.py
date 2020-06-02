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

    def lengthOfLongestSubstring2(self, s): # alternative: HashMap stores index of previous occurrence
        lookup, ans = {}, 0
        start = 0
        for end, v in enumerate(s):
            if v in lookup and lookup[v] >= start: # Python3 TypeError if comparing None to int
                start = lookup[v] + 1
            ''' OR
            if v in lookup:
            	start = max(start, lookup[v]+1)
            '''
            lookup[v] = end
            ans = max(ans, end - start + 1)
        return ans

print(Solution().lengthOfLongestSubstring3("abcabcbb")) # 3

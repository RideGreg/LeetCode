# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

    def lengthOfLongestSubstring2(self, s):
        map, ans = {}, 0
        start, end = 0, 0
        while end < len(s):
            while end < len(s) and s[end] not in map:
                map[s[end]] = end
                end += 1
            ans = max(ans, end-start)
            if end != len(s):
                newStart = map[s[end]] + 1
                for i in xrange(start, newStart):
                    del map[s[i]]
                start = newStart
        return ans

    def lengthOfLongestSubstring3(self, s):   # USE THIS, HashMap stores index; 'end' var for iteration, 'start' var is helper.
        map, ans = {}, 0
        start = 0
        for end in xrange(len(s)):
            if map.get(s[end]) >= start:
                ans = max(ans, end - start)
                start = map[s[end]] + 1
            map[s[end]] = end
        return max(ans, len(s) - start)

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")

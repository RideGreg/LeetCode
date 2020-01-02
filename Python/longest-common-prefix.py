# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

# 14
# Write a function to find the longest common prefix string
# amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


# Time:  O(n * k), k is the length of the common prefix
# Space: O(k)
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        
        for chars in zip(*strs): # zip stops when the shortest input iterable is exhausted. itertools.zip_longest()
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix
            
        return prefix

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["abcd", "abc", "ab"]))
    print(Solution().longestCommonPrefix(["hello", "heaven", "heavy"]))

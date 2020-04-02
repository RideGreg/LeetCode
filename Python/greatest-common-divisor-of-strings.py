# Time:  O(m + n)
# Space: O(1)

# 1071

# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself
# 1 or more times)
#
# Return the largest string X such that X divides str1 and X divides str2.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def check(s, common):
            i = 0
            for c in s:
                if c != common[i]:
                    return False
                i = (i+1)%len(common)
            return True
    
        def gcd(a, b):  # Time: O((logn)^2)
            while b:
                a, b = b, a % b
            return a
        
        if not str1 or not str2:
            return ""
        c = gcd(len(str1), len(str2))
        result = str1[:c]
        return result if check(str1, result) and check(str2, result) else ""

print(Solution().gcdOfStrings("ABCABC", str2 = "ABC"))
print(Solution().gcdOfStrings())
print(Solution().gcdOfStrings())
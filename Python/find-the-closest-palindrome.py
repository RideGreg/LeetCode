# Time:  O(l)
# Space: O(l)

# Given an integer n, find the closest integer (not including itself), which is a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two integers.
#
# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        candidates = set((str(10**l + 1), str(10**(l - 1) - 1)))
        prefix = int(n[:(l + 1)/2])   # first half of string
        for i in map(str, (prefix-1, prefix, prefix+1)):
            # if l even, select i; if l odd, select i w/o the last digit; [::-1] reverse order
            candidates.add(i + [i, i[:-1]][l%2][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

    def nearestPalindromic_bruteforce(self, n):
        delta = 1

        def isPalindrome(s):
            for i in xrange(len(s)/2):
                if s[i] != s[-1-i]:
                    return False
            return True

        while True:
            nint = int(n)
            if isPalindrome(str(nint - delta)):
                return str(nint - delta)
            if isPalindrome(str(nint + delta)):
                return str(nint + delta)
            delta += 1

        return ''


    def nearestPalindromic_ming(self, n): #better readability
        l = len(n)
        rets = set([10**l+1, 10**(l-1)-1])
        firstHalf = int(n[:(l+1)/2]) #
        for m in map(str, [firstHalf-1, firstHalf, firstHalf+1]):
            if l%2:
                m += m[::-1][1:]
            else:
                m += m[::-1]
            if m != n:
                rets.add(int(m))
        ans = min(rets, key=lambda x: (abs(x-int(n)), x))
        return str(ans)

if __name__ == "__main__":
    print Solution().nearestPalindromic("5")
    print Solution().nearestPalindromic("22")
    print Solution().nearestPalindromic("25")
    print Solution().nearestPalindromic("123")
    print Solution().nearestPalindromic("5432")

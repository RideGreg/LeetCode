# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set

# 1316 biweekly contest 17 1/11/2020

# Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string
# with itself (i.e. it can be written as a + a where a is some string).

try:
    xrange
except NameError:
    xrange = range

class Solution(object):
    def distinctEchoSubstrings(self, text): # USE THIS
        """
        :type text: str
        :rtype: int
        """
        def KMP(text, start, result): # only use KMP's getPrefix API, not do pattern search
            prefix = [-1]*(len(text)-start)
            j = -1
            for i in xrange(1, len(prefix)):
                while j > -1 and text[start+j+1] != text[start+i]:
                    j = prefix[j]
                if text[start+j+1] == text[start+i]:
                    j += 1
                prefix[i] = j

                total, rightPart = i + 1, i - j
                q, r = divmod(total, rightPart)
                if (j+1) and r == 0 and q % 2 == 0:
                    result.add(text[start:start+i+1])

            excludeSuffix = len(prefix)-(prefix[-1]+1)
            return excludeSuffix if prefix[-1]+1 and len(prefix) % excludeSuffix == 0 \
                   else float("inf")

        result = set()
        i, l = 0, len(text)-1
        while i < l:  # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefabcdefabcdef
            l = min(l, i + KMP(text, i, result))
            i += 1
        return len(result)


# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set
class Solution2(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        result = set()
        for l in xrange(1, len(text)//2+1):
            count = sum(text[i] == text[i+l] for i in xrange(l))
            for i in xrange(len(text)-2*l):
                if count == l:
                    result.add(text[i:i+l])
                count += (text[i+l] == text[i+l+l]) - (text[i] == text[i+l])
            if count == l:
                result.add(text[len(text)-2*l:len(text)-2*l+l])
        return len(result)

# rolling hash
# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set
class Solution3(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        MOD = 10**9+7
        D = 27  # a-z and ''
        result = set()
        for i in xrange(len(text)-1):
            left, right, pow_D = 0, 0, 1
            for l in xrange(1, min(i+2, len(text)-i)):
                left = (D*left + (ord(text[i-l+1])-ord('a')+1)) % MOD
                right = (pow_D*(ord(text[i+l])-ord('a')+1) + right) % MOD
                if left == right:  # assumed no collision
                    result.add(left)
                pow_D = (pow_D*D) % MOD 
        return len(result)


# Time:  O(n^3 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set
class Solution_TLE(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        def compare(text, l, s1, s2):
            for i in xrange(l):
                if text[s1+i] != text[s2+i]:
                    return False
            return True

        MOD = 10**9+7
        D = 27  # a-z and ''
        result = set()
        for i in xrange(len(text)):
            left, right, pow_D = 0, 0, 1
            for l in xrange(1, min(i+2, len(text)-i)):
                left = (D*left + (ord(text[i-l+1])-ord('a')+1)) % MOD
                right = (pow_D*(ord(text[i+l])-ord('a')+1) + right) % MOD
                if left == right and compare(text, l, i-l+1, i+1):
                    result.add(text[i+1:i+1+l])
                pow_D = (pow_D*D) % MOD 
        return len(result)

class Solution_ming:
    def distinctEchoSubstrings(self, text: str) -> int:
        n, ans, aset = len(text), 0, set()
        for sz in range(2, n+1, 2):
            for l in range(n+1-sz):
                r = l+sz-1
                k = l+sz//2-1
                if text[l:k+1] == text[k+1:r+1] and text[l:r+1] not in aset:
                    aset.add(text[l:r+1])
                    ans += 1
        return ans


print(Solution().distinctEchoSubstrings("abcabcabc")) # 3 "abcabc", "bcabca" and "cabcab"
print(Solution().distinctEchoSubstrings("leetcodeleetcode")) # 2 "ee" and "leetcodeleetcode"
print(Solution().distinctEchoSubstrings("aaaabbccbbcc")) # 5 'aa', 'aaaa', 'bb', 'cc', 'bbccbbcc'
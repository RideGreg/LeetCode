# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set

# 1316 biweekly contest 17 1/11/2020

# Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string
# with itself (i.e. it can be written as a + a where a is some string).

class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        def KMP(text, l, result):
            prefix = [-1]*(len(text)-l)
            j = -1
            for i in xrange(1, len(prefix)):
                while j > -1 and text[l+j+1] != text[l+i]:
                    j = prefix[j]
                if text[l+j+1] == text[l+i]:
                    j += 1
                prefix[i] = j
                if (j+1) and (i+1) % ((i+1) - (j+1)) == 0 and \
                   (i+1) // ((i+1) - (j+1)) % 2 == 0:
                    result.add(text[l:l+i+1])
            return len(prefix)-(prefix[-1]+1) \
                   if prefix[-1]+1 and len(prefix) % (len(prefix)-(prefix[-1]+1)) == 0 \
                   else float("inf")

        result = set()
        i, l = 0, len(text)-1
        while i < l:  # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefabcdefabcdef
            l = min(l, i + KMP(text, i, result));
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

        '''
        n, ans, aset = len(text), 0, set()
        dp = [[text[i:j+1] for j in range(n)] for i in range(n)]
        for sz in range(2, n+1):
            for l in range(n+1-sz):
                r = l+sz-1
                for k in range(l, r):
                    #if dp[l][k] and dp[k][r+1] and dp[l][k]==dp[k][r+1]:
                    x, y = dp[l][k], dp[k+1][r]
                    if dp[l][k] == dp[k+1][r]:
                        dp[l][r] = dp[l][k]
                        if text[l:r+1] not in aset:
                            aset.add(text[l:r+1])
                            ans += 1
                        break
        return ans
        '''

print(Solution().distinctEchoSubstrings("abcabcabc")) # 3
print(Solution().distinctEchoSubstrings("leetcodeleetcode")) # 2
print(Solution().distinctEchoSubstrings("aaaabbccbbcc")) # 5
# Time:  O(n)
# Space: O(1)

# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True
# if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
# Note:
# - A and B will have length at most 100.

# Rabin-Karp Algorithm (rolling hash)
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        Our approach comes down to quickly checking whether B is a substring of A2 = A+A. Specifically, check whether
        B = A2[0:N], or B = A2[1:N+1], or B = A2[2:N+2] and so on. To check this, we can use a rolling hash.

        Algorithm
        For a string S, say hash(S) = (S[0] * P^0 + S[1] * P^1 + S[2] * P^2 + ...) % MOD, where S[i] is the ASCII code of the string at that index.
        The idea is that hash(S) has output that is approximately uniformly distributed between [0, 1, 2, ..., MOD-1],
        and so if MOD is big enough and hash(S) == hash(T) it is very likely that S == T.

        Say we have a hash hash(A), and we want the hash of A[1], A[2], ..., A[N-1], A[0]. We can subtract A[0] from the hash,
        divide by P, and add A[0] * P**(N-1). (Our division is done by multiplying by the modular inverse Pinv = pow(P, MOD-2, MOD).)
        """
        def check(index):
            return all(A[(i+index) % len(A)] == c
                       for i, c in enumerate(B))

        if len(A) != len(B):
            return False

        M, p = 10**9+7, 113
        p_inv = pow(p, M-2, M)

        b_hash, power = 0, 1
        for c in B:
            b_hash += power * ord(c)
            b_hash %= M
            power = (power*p) % M

        a_hash, power = 0, 1
        for i in xrange(len(B)):
            a_hash += power * ord(A[i%len(A)])
            a_hash %= M
            power = (power*p) % M

        if a_hash == b_hash and check(0): return True

        power = (power*p_inv) % M
        for i in xrange(len(B), 2*len(A)):
            a_hash = (a_hash-ord(A[(i-len(B))%len(A)])) * p_inv
            a_hash += power * ord(A[i%len(A)])
            a_hash %= M
            if a_hash == b_hash and check(i-len(B)+1):
                return True

        return False


# Time:  O(n)
# Space: O(n)
# KMP algorithm
class Solution2(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        Intuition
        We want to find whether B exists in A+A. The KMP algorithm is a textbook algo. that does string matching in linear time, faster than brute force.

        Algorithm
        The algorithm is broken up into two steps, building the shifts table (or failure table), and using it to find whether a match exists.

        The shift table tells about the largest prefix of B that ends here. More specifically,
        B[:shifts[i+1]] == B[i - shifts[i+1] : i] is the largest possible prefix of B ending before B[i].

        We use a dynamic programming approach to build the shift table, where all previously calculated values of shifts are correct.
        Then, left will be the end of the candidate prefix of B, and right will be the end of the candidate section that
        should match the prefix B[0], B[1], ..., B[left]. Call positions (left, right) "matching" if the prefix ending
        at B[left] matches the same length string ending at B[right]. The invariant in our loop will be that
        (left-1, right-1) is matching by the end of each for-block.

        In a new for-block, if (left, right) is matching (ie. (left - 1, right - 1) is matching from before,
        plus B[left] == B[right]), then we know the shift (right - left) is the same number as before.
        Otherwise, when (left, right) is not matching, we need to find a shorter prefix.

        Our strategy is to find a matching of (left2, right) where left2 < left, by finding matchings
        (left2 - 1, right - 1) plus checking B[left2] == B[right]. Since (left - 1, right - 1) is a matching,
        by transitivity we want to find matchings (left2 - 1, left - 1). The largest such left2 is left2 = left - shifts[left].
        We repeatedly check these left2's in greedy order from largest to smallest.

        To find a match of B in A+A with such a shift table ready, we employ a similar strategy. We maintain a matching
        (match_len - 1, i - 1), where these positions correspond to strings of length match_len that end at B[match_len - 1] and (A+A)[i-1] respectively.

        Now when trying to find the largest length matching for (A+A) at position i, it must be at most (match_len - 1) + 1,
        where the quantity in brackets is the largest length matching to position i-1.

        Again, our strategy is to find a matching (match_len2 - 1, i - 1) plus check that B[match_len2] == (A+A)[i].
        Similar to before, if B[match_len] != (A+A)[i], then because (match_len - 1, i - 1) was a matching,
        by transitivity (match_len2 - 1, match_len - 1) must be a matching, of which the largest is found by
        match_len2 = match_len - shifts[match_len]. We also repeatedly check these match_len's in order from largest to smallest.

        If at any point in this algorithm our match length is N, we've found B in A+A successfully.
        """
        def strStr(haystack, needle):
            def KMP(text, pattern):
                prefix = getPrefix(pattern)
                j = -1
                for i in xrange(len(text)):
                    while j > -1 and pattern[j + 1] != text[i]:
                        j = prefix[j]
                    if pattern[j + 1] == text[i]:
                        j += 1
                    if j == len(pattern) - 1:
                        return i - j
                return -1

            def getPrefix(pattern):
                prefix = [-1] * len(pattern)
                j = -1
                for i in xrange(1, len(pattern)):
                    while j > -1 and pattern[j + 1] != pattern[i]:
                        j = prefix[j]
                    if pattern[j + 1] == pattern[i]:
                        j += 1
                    prefix[i] = j
                return prefix

            if not needle:
                return 0
            return KMP(haystack, needle)

        if len(A) != len(B):
            return False
        return strStr(A*2, B) != -1


# Time:  O(n^2)
# Space: O(1)
class Solution3(object):
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in xrange(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in xrange(len(A))):
                return True
        return False

# Time:  O(n^2)
# Space: O(n)
# Brute force
class Solution4(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A*2

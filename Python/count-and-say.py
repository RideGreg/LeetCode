# Time:  O(n * 2^n)
# Space: O(2^n)
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#

class Solution:
    # @return a string
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            ns = ''
            c = 1
            for i in range(len(s)):
                if i < len(s)-1 and s[i] == s[i+1]:
                    c += 1
                else:
                    ns += str(c)+s[i]
                    c = 1
            s = ns
        return s


    def countAndSay_kamyu(self, n):
        seq = "1"
        for i in xrange(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq

if __name__ == "__main__":
    for i in range(1, 6):
        print(Solution().countAndSay(i)) # 1, 11, 21, 1211, 111221



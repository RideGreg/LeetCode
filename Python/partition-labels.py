# Time:  O(n)
# Space: O(n)

# 763
# A string S of lowercase English letters is given. We want to partition this string into as many parts
# as possible so that each letter appears in at most one part, and return a list of integers representing
# the size of these parts.

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lookup = {c: i for i, c in enumerate(S)}
        first, last = 0, 0
        result = []
        for i, c in enumerate(S):
            # continue to extend the last position of current part
            last = max(last, lookup[c])
            if i == last:
                result.append(i-first+1)
                first = i+1
        return result

    # build and merge intervals. Codes are more than Greedy algorithm which scans twice.
    # Since at most 26 intervals, merge should be quick
    def partitionLabels2(self, S):
        first, last = [None] * 26, [None] * 26
        for i, c in enumerate(S):
            pos = ord(c) - ord('a')
            if first[pos] is None:
                first[pos] = i
            last[pos] = i

        intvl = []
        for b, e in zip(first, last):
            if b is not None:
                intvl.append([b, e])
        intvl.sort()

        ans = [intvl[0]]
        for b, e in intvl[1:]:
            if b < ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([b, e])
        return [e - b + 1 for b, e in ans]

print(Solution().partitionLabels("ababcbacadefegdehijhklij")) # [9,7,8]
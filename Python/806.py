class Solution(object):
    def numberOfLines(self, widths, S):
        lines, cur = 1, 0
        for c in S:
            if cur + widths[ord(c)-ord('a')] > 100:
                lines += 1
                cur = 0
            cur += widths[ord(c)-ord('a')]
        return [lines, cur]

print Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz")
print Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
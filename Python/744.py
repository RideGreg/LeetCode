class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if letters[-1] <= target:
            return letters[0]
        for l in letters:
            if l > target:
                return l

print Solution().nextGreatestLetter(["c", "f", "j"], 'k')#c
print Solution().nextGreatestLetter(["c", "f", "j"], 'c')#f
print Solution().nextGreatestLetter(["c", "f", "f", "j"], 'f')#j
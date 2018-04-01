class Solution(object):
    def uniqueMorseRepresentations(self, words):
        lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for w in words:
            ans.add(''.join(lookup[ord(c)-ord('a')] for c in w))
        print ans
        return len(ans)

print Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
# Time:  O(n)
# Space: O(n)

# 1407
# Given a string S of lowercase letters, a duplicate removal consists of choosing 
# TWO adjacent and equal letters, and removing them.

# We repeatedly make duplicate removals on S until we no longer can.

# Return the final string after all such duplicate removals have been made.  
# It is guaranteed the answer is unique.


# OPEN QUESTION: removeAllConseccutive seems a ill-formed question, e.g.
# 'abbbaaab' => 'b' if forward scan, but 'a' if backward scan. A better
# question is to remove every k consecutive repeated char, see 
# remove-all-adjacent-duplicates-in-string-ii.py

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for c in S:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)
        return "".join(result)


    # Multi Replace Time (n^2) while may execute n/2 times
    def removeDuplicates2(self, S: str) -> str:
        # generate 26 possible duplicates
        from string import ascii_lowercase
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S
            

print(Solution().removeDuplicates("abbaca")) # 'ca'

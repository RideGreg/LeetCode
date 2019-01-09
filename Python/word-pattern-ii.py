# Time:  O(n * C(n - 1, c - 1)), n is length of str, c is unique count of pattern,
#                                there are H(n - c, c - 1) = C(n - 1, c - 1) possible splits of string,
#                                and each one costs O(n) to check if it matches the word pattern.
# Space: O(n + c)

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2w, usedw = {}, set()
        return self.match(pattern, str, 0, 0, p2w, usedw)


    def match(self, pattern, str, i, j, p2w, usedw):
        if i == len(pattern) and j == len(str):
            return True
        elif i < len(pattern) and j < len(str):
            p = pattern[i]
            if p in p2w:
                w = p2w[p]
                if w == str[j:j+len(w)]:  # Match pattern.
                    return self.match(pattern, str, i + 1, j + len(w), p2w, usedw)
                return False
            else:
                for k in xrange(j, len(str)):  # Try any possible word
                    if len(str) - k < len(pattern) - i:
                        break
                    w = str[j:k+1]
                    if w not in usedw:
                        # Build mapping. Space: O(n + c)
                        p2w[p] = w
                        usedw.add(w)
                        if self.match(pattern, str, i + 1, k + 1, p2w, usedw):
                            return True
                        # backtrack
                        p2w.pop(p, None)
                        usedw.remove(w)
        return False


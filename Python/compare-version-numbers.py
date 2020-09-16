# Time:  O(n)
# Space: O(n)

# 165
# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2
# return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and
# contain only digits and the . character.
# The . character does not represent a decimal point and
# is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to
# version three", it is the fifth second-level revision of
# the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#
import itertools


class Solution(object):
    def compareVersion(self, version1, version2): # USE THIS
        def convert(s):
            arr = [int(x) for x in s.split('.')] # int() will remove leading zeros in each str segment
            while arr and arr[-1] == 0: # remove trailing zeros, alternatively we can appending trailing zeroes
                arr.pop()
            return arr

        v1, v2 = convert(version1), convert(version2)
        return 1 if v1 > v2 else -1 if v1 < v2 else 0


    # This saves space O(1), but too many codes to concatenate chars, not suitable for answering an interview question
    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n1, n2 = len(version1), len(version2)
        i, j = 0, 0
        while i < n1 or j < n2:
            v1, v2 = 0, 0
            while i < n1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < n2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
            j += 1

        return 0

# Time:  O(n)
# Space: O(n)


class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split("."), version2.split(".")

        if len(v1) > len(v2):
            v2 += ['0' for _ in range(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in range(len(v2) - len(v1))]

        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1

        return 0

    # cmp() was removed in Python3
    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        return cmp(v1, v2)

    def compareVersion3(self, version1, version2):
        splits = (map(int, v.split('.')) for v in (version1, version2))
        return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))


if __name__ == "__main__":
    print(Solution().compareVersion("21.0", "121.1.0")) # -1
    print(Solution().compareVersion("01", "1")) # 0
    print(Solution().compareVersion("1", "1.0")) # 0

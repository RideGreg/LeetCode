# Time:  O(nlogn * l), n is the length of files, l is the average length of strings
# Space: O(l)

# 937
# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has
# at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered
# lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in
# their original order. Return the final order of the logs.
#
# Example 1:
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
#
#
# Note:
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.

# Solution:
# Custom Sort. The rules are:
# - Letter-logs come before digit-logs;
# - Letter-logs are sorted alphanumerically, by content then identifier;
# - Digit-logs remain in the same order.

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def f(log):
            i, content = log.split(" ", 1)
            return (0, content, i) if content[0].isalpha() else (1,)
            # must have the comma in (1,), otherwise it is an int not tuple

        logs.sort(key=f)
        return logs

    # Time: O(nlogn * l), TAKE EXTRA Space: O(n*l)
    def reorderLogFiles_sortSeparately(self, logs):
        letterLog, digitLog = [], []
        for log in logs:
            if log[-1].isalpha():
                letterLog.append(log)
            else:
                digitLog.append(log)
        letterLog.sort(key = lambda x : (x[(x.index(' ')+1):], x))
        return letterLog+digitLog
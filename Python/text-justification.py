# Time:  O(n)
# Space: O(k), k is maxWidth.
# 68
# Given an array of words and a length L, format the text such that
# each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack
# as many words as you can in each line. Pad extra spaces ' '
# when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words,
# the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space
# is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def addSpaces(i, spaceCnt, spaceWidth):
            return (spaceWidth // spaceCnt) + int(i < spaceWidth % spaceCnt)

        def connect(begin, end, wordlength, is_last):
            s = []  # The extra space O(k) is spent here.
            for i in range(begin, end):
                s.append(words[i])
                if i < end - 1:
                    if is_last: # For the last line of text, it is left justified
                        s.append(' ')
                    else:
                        s.append(' ' * addSpaces(i - begin, end - begin - 1, maxWidth - wordlength))
            # For only one word in a line.
            line = "".join(s)
            if len(line) < maxWidth:    #!!! note this is not only for last line!!
                line += ' ' * (maxWidth - len(line))
            return line

        res = []
        begin, length = 0, 0
        for i in range(len(words)):
            if length + len(words[i]) + (i - begin) > maxWidth:
                res.append(connect(begin, i, length, False))
                begin, length = i, 0
            length += len(words[i])

        # Last line.
        res.append(connect(begin, len(words), length, True))
        return res


print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "just."], 16))
# ['This    is    an',
#  'example  of text',
#  'just aa.        ']

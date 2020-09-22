# Time:  O(n)
# Space: O(1)

# 1592
# You are given a string text of words that are placed among some number of spaces. Each word 
# consists of one or more lowercase English letters and are separated by at least one space. 
# It's guaranteed that text contains at least one word.

# Rearrange the spaces so that there is an equal number of spaces between every pair of 
# adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, 
# place the extra spaces at the end, meaning the returned string should be the same length as text.

# Return the string after rearranging the spaces.

class Solution(object):
    def reorderSpaces(self, text):
        spaces = text.count(' ')
        words = text.split()
        if len(words) > 1:
            q, r = divmod(spaces, len(words) - 1)
            return (' ' * q).join(words)  + ' ' * r
        else:
            return words[0] + ' ' * spaces


    # inplace solution
    def reorderSpaces_kamyu(self, text):
        """
        :type text: str
        :rtype: str
        """
        text = list(text)
        # count the spaces and words
        space_count, word_count = 0, 0
        for i, c in enumerate(text):
            if c == ' ':
                space_count += 1
            elif i == 0 or text[i-1] == ' ':
                word_count += 1

        # rearrange all the spaces to the right
        left, i = 0, 0
        while i < len(text):
            has_word = False
            while i < len(text) and text[i] != ' ':
                text[left], text[i] = text[i], text[left]
                left += 1
                i += 1
                has_word = True
            if has_word:
                left += 1  # keep one space
            i += 1

        # rearrange all the spaces to the left
        equal_count = space_count//(word_count-1) if word_count-1 > 0 else 0
        extra_count = space_count%(word_count-1) if word_count-1 > 0 else space_count
        right, i = len(text)-1-extra_count, len(text)-1
        while i >= 0:
            has_word = False
            while i >= 0 and text[i] != ' ':
                text[right], text[i] = text[i], text[right]
                right -= 1
                i -= 1
                has_word = True
            if has_word:
                right -= equal_count  # keep equal_count spaces
            i -= 1
        return "".join(text)

print(Solution().reorderSpaces("  this   is  a sentence   ")) # "this   is   a   sentence  "
print(Solution().reorderSpaces("hello  world ")) # "hello   world"
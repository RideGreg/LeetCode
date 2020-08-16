# Time:  O(1)
# Space: O(1)

# 681
# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
#
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(":")
        curr = int(h) * 60 + int(m)
        for i in range(curr+1, curr+1441):
            t = i % 1440
            h, m = divmod(t, 60)
            result = "{:0>2d}:{:0>2d}".format(h, m) # new format 
                                                  # "{:02d}:{:02d}".format(7, 3) => "07:03"   align default to > for number
                                                  # "{:0<2d}:{:0<2d}".format(7, 3) => "70:30"  fill,align,width,type
                                                  # "{:x>2d}:{:x>2d}".format(7, 3) => "x7:x3"  fill,align,width,type, doesn't work if remove >
                                                  # '7'.rjust(2, '0') => "07"
            # result = "%02d:%02d" % (h, m) # old format
            if set(result) <= set(time):
                return result

    def nextClosestTime2(self, time): # not using format, check each digits by bases
        bases = [600, 60, 10, 1]
        h, m = time.split(":")
        curr = int(h) * 60 + int(m)
        for i in range(1, 1441):
            res = ''
            t = (curr + i) % 1440
            for base in bases:
                digit = str(t // base) # check digit on each position
                if digit not in time:
                    break
                res += str(digit)
                t %= base
            if len(res) == 4:
                break

        return res[:2] + ':' + res[2:]

print(Solution().nextClosestTime("19:34")) # "19:39"
print(Solution().nextClosestTime("23:59")) # "22:22"

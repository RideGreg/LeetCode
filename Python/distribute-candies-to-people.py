# Time:  O(n + logc), c is the number of candies
# Space: O(1)

# 1103 weekly contest 143 6/29/2019

# We distribute some number of candies, to a row of num_people people in the following way:
#
# We then give 1 candy to the first person, 2 candies to the second person,
# and so on until we give n candies to the last person.
#
# Then, we go back to the start of the row, giving n + 1 candies to the
# first person, n + 2 candies to the second person, and so on until we
# give 2 * n candies to the last person.
#
# This process repeats (with us giving one more candy each time, and moving
# to the start of the row after we reach the end) until we run out of candies.
# The last person will receive all of our remaining candies (not necessarily
# one more than the previous gift).
#
# Return an array (of length num_people and sum candies) that represents
# the final distribution of candies.
#
#
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # find max integer p s.t. sum(1 + 2 + ... + p) <= C
        # => remaining : 0 <= C-(1+p)*p/2 < p+1
        # => -2p-2 < p^2+p-2C <= 0
        # => 2C+1/4 < (p+3/2)^2 and (p+1/2)^2 <= 2C+1/4
        # => sqrt(2C+1/4)-3/2 < p <= sqrt(2C+1/4)-1/2
        # => p = floor(sqrt(2C+1/4)-1/2)
        p = int((2*candies + 0.25)**0.5 - 0.5) 
        remaining = candies - (p+1)*p//2
        rows, cols = divmod(p, num_people)
        
        result = [0]*num_people
        for i in range(num_people):
            result[i] = (i+1)*(rows+1) + (rows*(rows+1)//2)*num_people if i < cols else \
                        (i+1)*rows + ((rows-1)*rows//2)*num_people
        result[cols] += remaining
        return result


# Time:  O(n + logc), c is the number of candies
# Space: O(1)
class Solution2(object): # USE THIS
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # find max integer p s.t. sum(1 + 2 + ... + p) <= C
        l, r = 1, candies
        while l < r:
            m = (l+r+1) // 2
            if m*(m+1)//2 < candies:
                l = m
            else:
                r = m - 1
        p = r
        remaining = candies - (p+1)*p//2
        rows, cols = divmod(p, num_people)
        
        result = [0]*num_people
        for i in range(num_people):
            result[i] = (i+1)*(rows+1) + (rows*(rows+1)//2)*num_people if i < cols else \
                        (i+1)*rows + ((rows-1)*rows//2)*num_people
        result[cols] += remaining
        return result


# Time:  O(sqrt(c) + n), c is the number of candies
# Space: O(1)
# assume total s step, s(s+1)//2 >= c => s^2 >= c => only need s>=sqrt(c)
class Solution3(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        result = [0]*num_people
        i = 0
        while candies != 0:
            result[i % num_people] += min(candies, i+1)
            candies -= min(candies, i+1)
            i += 1
        return result

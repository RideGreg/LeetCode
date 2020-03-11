# Time:  O(rlogr), r is the number of result
# Space: O(r)

# 1333 weekly contest 173 1/25/2020

# Given the array  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have
# to filter the restaurants using three filters.
#
# The veganFriendly filter will be either true (meaning you should only include restaurants with
# veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition,
# you have the filters maxPrice and maxDistance which are the maximum value for price and
# distance of restaurants you should consider respectively.
#
# Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest.
# For restaurants with the same rating, order them by id from highest to lowest. For simplicity
# veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.

class Solution(object):
    # USE THIS: filter + sort + retrieve
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        def foo(x):
            return x[2] >= veganFriendly and x[3] <= maxPrice and x[4] <= maxDistance

        ans = filter(foo, restaurants)
        return list(map(lambda x: x[0], sorted(ans, key=lambda x: (-x[1], -x[0]))))

    def filterRestaurants_kamyu(self, restaurants, veganFriendly, maxPrice, maxDistance):
        result, lookup = [], {}
        for j, (i, _, v, p, d) in enumerate(restaurants):
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                lookup[i] = j
                result.append(i)
        result.sort(key=lambda i: (-restaurants[lookup[i]][1], -restaurants[lookup[i]][0]))
        return result


print(Solution().filterRestaurants([
    [1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]
], 1, 50, 10)) # [3,1,5]
print(Solution().filterRestaurants([
    [1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]
], 0, 50, 10)) # [4,3,2,1,5]
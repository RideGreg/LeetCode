# Time:  O(nlogn)
# Space: O(n)

# 1169 weekly contest 151 8/24/2019
# A transaction is possibly invalid if:
# - the amount exceeds $1000, or;
# - if it occurs within (and including) 60 minutes of another transaction with the same name
# in a different city.
#
# Each transaction string transactions[i] consists of comma separated values representing
# the name, time (in minutes), amount, and city of the transaction.
#
# Given a list of transactions, return a list of transactions that are possibly invalid.
# You may return the answer in any order.

import collections


class Solution:
    def invalidTransactions(self, transactions):  # USE THIS
        import bisect
        AMOUNT, MINUTES = 1000, 60
        # preprocess data format
        trans = []
        for s in transactions:
            name, time, amt, city = s.split(',')
            trans.append((name, int(time), int(amt), city))

        # sort once upfront by time
        trans.sort(key=lambda t: t[1])
        # group by name
        lookup = collections.defaultdict(list)
        for i, t in enumerate(trans):
            lookup[t[0]].append((t[1], i))

        ans = []
        # list w/ different name is processed separately
        for indexes in lookup.values():
            for time, idx in indexes:
                t = trans[idx]
                if t[2] > AMOUNT:
                    ans.append("{},{},{},{}".format(*t))
                    continue

                l = bisect.bisect(indexes, (t[1]-MINUTES-1, idx))
                r = bisect.bisect(indexes, (t[1]+MINUTES+1, idx))
                for pos in range(l, r): # pos r should not be included
                    i = indexes[pos][1]
                    if trans[i][3] != t[3]:
                        ans.append("{},{},{},{}".format(*t))
                        break
        return ans


    # con: 1. no need to maintain separate dict for different cities, and do multiple binary search
    # 2. insort is expensive, should sort once upfront
    def invalidTransactions_mming(self, transactions):
        import collections, bisect
        lookup, ans = collections.defaultdict(dict), set()
        for i, s in enumerate(transactions):
            name, time, amt, city = s.split(',')
            time = int(time)
            amt = int(amt)
            if amt > 1000:
                ans.add(i)
            for cty, v in lookup[name].items(): # expensive, first get all other cities, then check time
                if cty != city:
                    left = bisect.bisect_left(v, (time - 60, -1))
                    right = bisect.bisect_right(v, (time + 60, 2000))
                    for j in range(left, right):
                        # because lookup lists were not populated in preprocess, cannot add i only, has to add both
                        ans.add(v[j][1])
                        ans.add(i)

            if city not in lookup[name]:
                lookup[name][city] = []
            bisect.insort(lookup[name][city], (time, i))
        return [transactions[i] for i in ans]


    # WRONG: suppose ['a,10,500,c1', 'a,11,500,c1', 'a,20,500,c2'], the first string not caught
    def invalidTransactions_wrong(self, transactions): #
        tlist = list(map(lambda x: x.split(','), transactions))
        tlist.sort(key=lambda x: (x[0], int(x[1]))) # KENG: sort int string '137'<'52'
        ans = set()
        for i, v in enumerate(tlist):
            if int(v[2]) > 1000:
                ans.add(i)
            if i:
                a, b = tlist[i-1], tlist[i] # this doesn't work by only checking the prev ONE item
                if a[0] == b[0] and int(b[1])-int(a[1])<=60 and a[3]!=b[3]:
                    ans.add(i-1)
                    ans.add(i)
        return [','.join(tlist[i]) for i in ans]

print(Solution().invalidTransactions([
    "alex,741,1507,barcelona",
    "bob,52,1152,beijing",
    "bob,210,261,beijing",
    "bob,220,105,beijing",  # omitted by invalidTransactions_wrong()
    "bob,237,645,barcelona",
    "bob,607,14,amsterdam",
    "xnova,914,715,beijing",
    "alex,279,632,beijing"]))
# ['bob,52,1152,beijing', 'bob,210,261,beijing', 'bob,220,105,beijing', 'bob,237,645,barcelona',
# 'alex,741,1507,barcelona']

print(Solution().invalidTransactions([
    "alex,676,260,bangkok",
    "bob,656,1366,bangkok",
    "alex,393,616,bangkok",
    "bob,820,990,amsterdam",
    "alex,596,1390,amsterdam"])) # ["bob,656,1366,bangkok","alex,596,1390,amsterdam"]
print(Solution().invalidTransactions([
    "bob,689,1910,barcelona",
    "alex,696,122,bangkok",
    "bob,832,1726,barcelona",
    "bob,820,596,bangkok",
    "chalicefy,217,669,barcelona",
    "bob,175,221,amsterdam"])) # ["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]
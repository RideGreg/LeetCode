class Solution(object):
    def accountsMerge(self, accounts):
        emails, ids, id = {}, {}, 1
        for a in accounts:
            a=[a[0]]+list(set(a[1:]))
            old_ids = set()
            for email in a[1:]:
                if email in emails:
                    old_ids.add(emails[email])
            if len(old_ids) == 0:
                ids[id] = a
                emails.update(dict((e, id) for e in a[1:]))
                id += 1
            else:
                l = list(old_ids)
                # merge curr list
                emails.update(dict((e, l[0]) for e in a[1:]))
                for e in a[1:]:
                    if e not in ids[l[0]]:
                        ids[l[0]].append(e)
                # merge old list
                for id_merge in l[1:]:
                    for e in ids[id_merge][1:]:
                        emails[e] = l[0]
                        if e not in ids[l[0]]:
                            ids[l[0]].append(e)
                    del ids[id_merge]
        res = []
        for k, id in ids.iteritems():
            res.append([id[0]]+sorted(id[1:]))
        return res


print Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])
#print Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])

#print Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnnybravo@mail.com","johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])

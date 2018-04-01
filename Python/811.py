class Solution(object):
    def subdomainVisits(self, cpdomains):
        import collections
        ans = collections.defaultdict(int)
        for d in cpdomains:
            cnt, addr = d.split()
            ans[addr] += int(cnt)
            while '.' in addr:
                addr = addr.split('.', 1)[-1]
                ans[addr] += int(cnt)
        return [str(v)+' '+k for k, v in ans.iteritems()]

print Solution().subdomainVisits(["900 discuss.leetcode.com"])
print Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
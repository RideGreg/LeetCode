class Solution:
    def wordSort(self, alphabet, words):
        lookup = {}
        for i, c in enumerate(alphabet):
            lookup[c] = i

        def myCmp(s1, s2):
            if s1 == s2: return 0
            i, j = 0, 0
            while i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                i, j = i+1, j+1
            return -1 if i == len(s1) else 1 if j==len(s2) else -1 if lookup[s1[i]]<lookup[s2[j]] else 1

        words.sort(myCmp) # also ok: words.sort(cmp=myCmp) sorted(words,myCmp) sorted(words,cmp=myCmp);
                          #  not ok: words.sort(key=myCmp) sorted(words,key=myCmp)

        return words

print Solution().wordSort("zbadefghijklmnopqrstuvwxyc",["b","bbb","bb"])
print Solution().wordSort(
    ['c','b','a','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
                          ['cab','cba','abc'])
print Solution().wordSort(
    ['z','b','a','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','c'],
                          ['bca','czb','za','zba','ade'])
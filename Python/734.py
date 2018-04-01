class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        ht = {}
        for pair in pairs:
            if pair[0] not in ht:
                ht[pair[0]] = {pair[1]}
            else:
                ht[pair[0]].add(pair[1])
            if pair[1] not in ht:
                ht[pair[1]] = {pair[0]}
            else:
                ht[pair[1]].add(pair[0])
        print ht
        for i, word in enumerate(words1):
            if word != words2[i] and ((word not in ht) or words2[i] not in ht[word]):
                return False
        return True
'''
print Solution().areSentencesSimilar( \
    ['great', 'acting', 'skills'], \
    ["fine", "drama", "talent"], \
    [["great", "fine"], ["acting","drama"], ["skills","talent"]] )
print Solution().areSentencesSimilar( \
    ['great', 'acting', 'skills'], \
    ["fine", "drama", "talent"], \
    [["great", "fine"], ["acting","drama"]] )'''
print Solution().areSentencesSimilar( \
    ["an","extraordinary","meal"],
    ["one","good","dinner"],
    [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],\
     ["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],\
     ["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],\
     ["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],\
     ["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],\
     ["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],\
     ["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],\
     ["possess","own"],["keep","own"],["have","own"],["extremely","very"],\
     ["actually","very"],["really","very"],["super","very"]])



class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cont = True
        curr = self.root
        for id, c in enumerate(word,1):
            if not c in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]

            if not curr.is_string and id != len(word):
                cont = False
                print "set False 2 ", c
        curr.is_string = True
        return cont

class Solution(object):
    def longestWord(self, words):
        res = ''
        words = sorted(words)
        d = WordDictionary()
        for w in words:
            cont = d.addWord(w)
            print w, cont
            if cont and len(w) > len(res):
                res = w
        return res
'''
class Solution {
public:
    string longestWord(vector<string>& words) {
        unordered_set<string> dict(words.begin(), words.end());
        
        string ans = "";
        for(auto s : words)
        {
            string bk = s;
            while(!s.empty() && dict.find(s) != dict.end()) s.pop_back();
            if(s.empty())
            {
                if(bk.size() > ans.size()) ans = bk;
                else if(bk.size() == ans.size() && bk < ans) ans = bk;
            }
        }
        return ans;
    }
};
'''

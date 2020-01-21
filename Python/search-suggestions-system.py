# Time:  ctor: O(n * l), n is the number of products
#                      , l is the average length of product name
#        suggest: O(l^2)
# Space: O(t), t is the number of nodes in trie


# 1268 weekly contest 164 11/23/2019

# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common prefix
# with the searchWord. If there are more than three products with a common prefix
# return the three lexicographically minimums products.
#
# Return list of lists of the suggested products after each character of searchWord is typed.

import collections


class TrieNode(object):
    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode)
        self.infos = [] # store the index of top 3 words going through this node

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.infos.append(i)
            curr.infos.sort(key=lambda x: words[x])
            if len(curr.infos) > self.__TOP_COUNT:
                curr.infos.pop()


class Solution(object):  # USE THIS: better to be slow in trie building time, and fast in query
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # build trie
        root = TrieNode()
        for i in range(len(products)):
            root.insert(products, i)

        # query trie
        result = [[] for _ in range(len(searchWord))]
        cur = root
        for i, c in enumerate(searchWord):
            if c not in cur.leaves:
                break
            cur = cur.leaves[c]
            result[i] = [products[x] for x in cur.infos]
        return result


# Time:  ctor: O(n * l * log(n * l)), n is the number of products
#                                   , l is the average length of product name
#        suggest: O(l^2)
# Space: O(t), t is the number of nodes in trie
class TrieNode2(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode2)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(i)

    def add_info(self, i):
        if len(self.infos) == self.__TOP_COUNT:
            return
        self.infos.append(i)


class Solution2(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        trie = TrieNode2()
        for i in range(len(products)):
            trie.insert(products, i)
        result = [[] for _ in range(len(searchWord))]
        for i, c in enumerate(searchWord):
            if c not in trie.leaves:
                break
            trie = trie.leaves[c]
            result[i] = [products[x] for x in trie.infos]
        return result


# Time:  ctor: O(n * l * log(n * l)), n is the number of products
#                                   , l is the average length of product name
#        suggest: O(l^2 * n)
# Space: O(n * l)
import bisect


class Solution3(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()  # Time: O(n * l * log(n * l))
        result = []
        prefix = ""
        for i, c in enumerate(searchWord):  # Time: O(l)
            prefix += c
            start = bisect.bisect_left(products, prefix)  # Time: O(log(n * l))
            new_products = []
            for j in xrange(start, len(products)):  # Time: O(n * l)
                if not (i < len(products[j]) and products[j][i] == c):
                    break
                new_products.append(products[j])
            products = new_products
            result.append(products[:3])
        return result


# not store top 3 within trie in build time; have to dfs to find top 3 words in query.
# get "RecursionError: maximum recursion depth exceeded" for very long input (1st testcase)
class Node:
    def __init__(self):
        self.is_string = False
        self.leaves = collections.defaultdict(Node)

class Solution_ming:
    def suggestedProducts(self, products, searchWord):
        def dfs(cur, res):
            if len(ss) < 3:
                if cur.is_string:
                    ss.append(res)

                for k in sorted(cur.leaves):
                    dfs(cur.leaves[k], res+k)

        root = Node()
        for p in products:
            cur = root
            for c in p:
                cur = cur.leaves[c]
            cur.is_string = True

        ans = []
        cur, res = root, ''
        for c in searchWord:
            if cur and c in cur.leaves:
                cur = cur.leaves[c]
                res += c
                ss = []
                dfs(cur, res)
                ans.append(ss)
            else:
                ans.append([]) # better to have ans pre-populated with required length
                cur = None

        return ans

#print(Solution().suggestedProducts(["usepzmuywcnicnglsohczkvmbmtfrkwsvbrmbwvehbzpqmiznwvyurtnpwdglycydwgelnsulelgeiweaamsvqmhnxsrjtsgeylvfujgdjhailtpkbqzmzdtplqzoafsojdjrhoranjuxjuuigztefsifutmdazwqoxwaxxyetgumfbppuowtogpqxcmrvqloeutkppmflczgmspzskfdlxcjbadmucoiqjnjhtjcoczjfwccvmqwqslrbeewcesebdortkcsgjdpyhxlswqlzjacxltcaoirsdtzcxgnuouyvmflmyocfvqxkhpluuprdeuppnuwgucmjbjdbnksnriatirwbdrdzemfkomvahskcnonxvpxwmkomzurplzigdhrziuvkyjcynffykgvfbaunfeppmhwqaipycqrldnxqzgxtompwkedbfmbamghsmvxlqwrndxnincfpldzmuvoywvdxgkurahlrbhjahmanfhjrmalpdzfycyyfwrvocxvakfwxpxliyjxnvcfohwoogckjvppnhxpuameuiinjerlqwmtyoevrwtfhkzkdrtwgtbhttiqzawakkpemlkwfcvnsndvqpqvllbonbijrrujtmzfontnokkjadmsrjgogfnjmtghndneqotrqjfzkndjxulyslllnjmwqbqqjtqegykbnoodvfxmbmwuvdmcqivjoaedxkhrbqthxwezlsjexfifqgcktgftzkusjousanslifuhqyutopzrhnlohvszpntofhyxlvdvtrisngpqiegbkptnebakphswxbdvftpaxkoabebceoeoqbbwlbhvthbuqlbwghpxjhwamanrzfuaqzfwsyenupkfpsvzafjsykksdzsczbdzqreyxgkbmmsqroubjwasqewazzppkjyromhorjslcjijizbhijyubivqryncoyahgftzcdjjysrsdikfwkxlvwclivpijgworgjoizn"],
#                                    "usepzmuywcnicnglsohczkvmbmtfrkwsvbrmbwvehbzpqmiznwvyurtnpwdglycydwgelnsulelgeiweaamsvqmhnxsrjtsgeylvfujgdjhailtpkbqzmzdtplqzoafsojdjrhoranjuxjuuigztefsifutmdazwqoxwaxxyetgumfbppuowtogpqxcmrvqloeutkppmflczgmspzskfdlxcjbadmucoiqjnjhtjcoczjfwccvmqwqslrbeewcesebdortkcsgjdpyhxlswqlzjacxltcaoirsdtzcxgnuouyvmflmyocfvqxkhpluuprdeuppnuwgucmjbjdbnksnriatirwbdrdzemfkomvahskcnonxvpxwmkomzurplzigdhrziuvkyjcynffykgvfbaunfeppmhwqaipycqrldnxqzgxtompwkedbfmbamghsmvxlqwrndxnincfpldzmuvoywvdxgkurahlrbhjahmanfhjrmalpdzfycyyfwrvocxvakfwxpxliyjxnvcfohwoogckjvppnhxpuameuiinjerlqwmtyoevrwtfhkzkdrtwgtbhttiqzawakkpemlkwfcvnsndvqpqvllbonbijrrujtmzfontnokkjadmsrjgogfnjmtghndneqotrqjfzkndjxulyslllnjmwqbqqjtqegykbnoodvfxmbmwuvdmcqivjoaedxkhrbqthxwezlsjexfifqgcktgftzkusjousanslifuhqyutopzrhnlohvszpntofhyxlvdvtrisngpqiegbkptnebakphswxbdvftpaxkoabebceoeoqbbwlbhvthbuqlbwghpxjhwamanrzfuaqzfwsyenupkfpsvzafjsykksdzsczbdzqreyxgkbmmsqroubjwasqewazzppkjyromhorjslcjijizbhijyubivqryncoyahgftzcdjjysrsdikfwkxlvwclivpijgworgjoizn"))

print(Solution().suggestedProducts([
    "mobile","mouse","moneypot","monitor","mousepad"], "mouse"
))
# [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad", "m"], "m")) #[['m']]
print(Solution().suggestedProducts(["havana"], "havana"))
# [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
print(Solution().suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
print(Solution().suggestedProducts(["havana"], "tatiana"))
# [[],[],[],[],[],[],[]]
'''
print(Solution().suggestedProducts(
["eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrojt","mervtkzsouapfbky","eucgsmpsyndddijvpxfagngnjbzxuajxnzjk","eduvadjohhskmyzipulgjeat","eucgsnatcadpbcyrxlgldpcaijmnojdkjqfwxkz","eucgsmpsynevhpeoqwbgdidv","yvu","eucgsmpsyndddijvpxfagnbjthdmywjcmbmgpfrvwhdarjske","eixctybvrnuyqibnpxpbcpcqcq","eucgsmpsyndddijvpxfagngnjrcnbbwae","lrvlimn","eucgsmpsyndddijvpxfagngnjbzgsidschcqhm","thhnadanjkbrcnofgpdfthvcodrmrezulkuytrqosqaooecqom","eucgsmpsyndddijvpxfagngwcpixbrkupusfqoyihroghoae","eucgsmpsyndddijvpxmmydswjxsdmer","fhfhindvjohibmsoipvdyedlxoinlumjlb","lsuinsmrgxxhswxshvogzxojsbvhzbcioldypag","ptbyxfktngjsofvicpvsmyqddacyahf","yjhiemwpwfpyewvcfbtljsrwlfiihwisqekfoearodlvhoejq","atoygkvdbdvmuukgfjnufsnhjcsaxk","eucgsdwqeaslgrthiruatrpulqyjgmsbdljebf","eucgsmpsyndddijvpxpcyrilzawoid","eucgsmpsyndddijvpxfagngnjbhvxvjmecfdqzpokhzpqdo","faoywdrvlgacdcfj","eucgsmpsynddwdgwnssfvds","eucgsmpsyndqgjneynofkuebob","asafyzzpxlltqyscywuahwinwijuccwnd","eucgsmpsyndddiznbxfvpqei","eucgsmpsyndddijvpximqtdtlybvziqhdvowuijbkurk","hvxmdjutynhrxyubizbyjwwxfpvblzxvfrca","eucgsu","jhckeuhdvbfdzmyjbjcfariwejezwhtzojeyhxjwegqgrl","eucgsmpsyndddijvpxfagngnjsjjbob","eucgsmpsyndddijvpxfdtbeujjoeqvezdjmopfcmzohuantaid","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszloha","eucgsmpsyndddijvpxfagngnjbzxuajlkwhlwhuwmyagdvymu","jdskdhwkehgqazzweqyzmqzsikjnwgylnhgugjixyrpmyrs","eucgsmpsdney","sasmjvaqjrrovkxqccfpqyruscxgzkbeekz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjjofldab","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdros","ekszgjqykwcwatzrzykatpxcasaifohwrrhipm","shfcpdjhktwfcqezsabkzyzyuibxpzxggnxgcwflloucbgodpm","tpcxhiehypiqtaxzdjxhofufucblqvkoqhlgxgozolaelf","swtrepxomxqemgodrupgigvpxxgptmilfkmzhfnr","dcvzdk","eucgsmpsyndddijvpxfagngnjbzxuajxmrmssckqdpjjasnms","nknhhv","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwjyi","qrsqrmqtpajtewxiegcevy","eucgsmpsyndddijvpxfagnfqcq","eucgsmpsyndddijvpxfagngnjbzxuajxmicjxmxhnrxbbczh","eucgshcaieewetzvzwigqfrlwpy","ogubeczu","eucgsmpsyndddijvpxfagngnjbzxuavqyzgaeyi","eucgsmpsyndddijvpxfagngnjbzxuajxmonbleriwyuvlnsfzt","jhz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdroje","xasvjrkqyxory","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwsehufy","eucgsmpsyndntjxkzpjstoke","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszhwsbfrppvadx","eucgsmrczev","eucgsmpsyndddijvpxfagngnjbzxuafelaasrnq","eucgsmpsyndddijvpxohsjopdnlnlhksjadjvuvroybu","gnntehraxahinoyqdrspmjaunucrzw","roqdenkakwsbkcbkijyrpfdehrfj","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgusf","eucgsmpsyndddijvpxfagngnjbjkffxzscalu","eugyortzihuywhfyrwubdfuomvcjudxtappednlohmxz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswq","eucjqsqvatpjbfvhowkaagxyidiyymapdumaxgoqgbpwsu","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrk","es","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdwv","kbninamhdqpoyzznnsqxzmieqajsqrjocrqbmfhwomstdc","jbwggbwtybranddatuybnzre","ludoupnbvsxksvmtaxuuiymidzotziwbqaclvvk","eucgsmpsyndddijvpxfagngnsgpnllzgpyirgem","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtebvruvqmpx","nwbqryotfdaopywffjbikuqzraabwngcicsufkeerbpnfyi","eucgsmpsyndddijvoaevblhxotmowpxwpuhzmemw","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgu","eucgsmpsyndddijvpcfjbzthtculbzszzfaroncw","grygljuxydgpoygjoemajbkaqmbwyverlruejnigqdsvdpwm","eucgsmpsyomtefhlwqluqgcckz","eucijltqylixpvjwtlhurqdseysduhivw","eucgsmpsyndddijvpxfagngnjbzxuajxmrbcm","zibchozkzyhdsmfcryjyzkzgyohjs","yiuxtmtzrnnitnpzyfgfctnlednanfwtjplvueab","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwslgknojn","eucgsmpsyndddijvpxfagngnjbxzehobuljrngufbcks","bwbbmbvwzegxmqhdmufnvwpwtykmdvwngqtdwym","eucgsmpsyndddijvpxfagnoezpyieslubwxeobrnktvnpinamb","eucgsmpslmkdakhg","eucgsmczlqunsmfbrodtrtevmuflaf","rpofbqaryrhmqzqkzrmhhsmtgfecva","pmvfbplrjqcmxlpypswxgqemjpxmwmswesrhwmicumoilapzhy","eucgsmpsyndddezzokejvhvdmsoaaoowwottmw","rmvmikeynztayityavakrt","tdeypjrxduem","fqvsmpnzkzuubhuwchdqy","eucgsmpsyoesekvyqvtmymaplhzynaupevoihscjkrjtcj","eucgsmpsyndddijvpxfagngnjbzxjh","jghjdzajfpvyesz","eucgsmpsyndddijvpxfagngnjbzxlmymsyqvaojj","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwdetn","eunahmcfpnnjavmduowjntsgo","eucgsmpsyndddijvpxfagngnjbzqinqttopi","ubgzjxnomgcnrbbhyppemgyejbycpgamympgupaetudz","mtuindengcxqg","eucgdxsvzyxpbwtnqmzundoosvddromqhydyyjich","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgkqoyw","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrog","eucgsmpsyndddijvpxfagnpcl","eucgsmpsyndddijvpxfagngnjbzjegcxjcrslyvgbd","nhb","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwsudaj","vnyfkvdguu","eucshaijqdl","eucgsmpsyndddijvpxfagngnjbzxuyxowpbndxvxayzxfp","fvgk","eucgsmpslzukdhnbtmsycj","wvpelpocfsodafurhbgbytnta","eucgsmpsyndddijvpxfagngnjbzzetehbbepo","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdayg","eucgsmpsyndddijvpxfagngnjbzxuajxjtkkz","knhrz","eucgsmpsyndddijvpxfagngnjbzxuyretdzgzkqaep","eucgsmpsyndddijvpxfagngnjbzxuajxmgi","eucgdjnclcqogrzxi","clliyxtdxzwwz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvvev","sugaphcopoyjzoxdpznrkrgjzcfdddvcktwxukcnan","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrojp","vwavfxqerifzseyfefbchueoadvcoximlvowsndrwxspqsn","ejafexrgcikuqefkvlfe","eucgsmpsyndddijvpxfaiuejxgpzbirbus","eucgsmpsyndddijvpxfagngnjbzzdo","bgtdtziavmvfbkexrmqzojkdrapfbljxghlesmflzvgxrooc","eucgsmpsyndddijvpxfagludvrubjhfhn","jsposqsidurgsqjwkabv","eucgsmpsyndddijvpxfagnplbcjevfnfaezqcijiixrrcd","wdhaxpoe","nkj","eucgsmpsyndddijvpxfagngnjbzxuajxmweazgncksq","eucgsmpsyndddijvpxfagnyxks","bouogc","eucgabxhtbnohgmunhrospjzqozczhowc","udcilqgipfjswuscpxtbgqancfolgqbvfvrzsy","eucgsmpsyndddijvpcdswmsvlekrtarkybjwovevieve","zkwfbyawpokgpnzzikaybfosdbqjmkdthsyoojb","gabgl","bkyxlqjgdsuhzbpvtnaobudwsrjqvceliadetviiar","eucgsmpsyndddijvpxfagngnjbzxuajxqqdlwpeyxgtuvbfqj","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswwvy","ryxcr","eucgsmpsyndddijvpxfagngnjbzvrkbgrrtcpbqvlktqwwxxn","eucgsmpsyndddijfagrxzrdg","eucgsmhsnicnajhcaca","revsyodsujynljmd","fficqqokrlkfwsbosapqvaurdk","eucgudniqtxzmtschgm","eucgsmpsyncxbvicmuafacp","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgjrp","qvjbtmibwikrugaeihweuumhajcffcurgn","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdcum","jolquz","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjyfpyyv","eucgsmpsyndddijvpxfagngnjbzxubimdvzlcpv","mesisdbvntasidlsnpbyrv","aekcjkuqrjfujvztrpiksbkegngbilgshwdgmfxz","fcmragokrxletuojnwflovikmovutvdzomlwyidpbzu","eucgsmpsynyozqjvjgnqtgxktlorcaij","eucgsqszvinjizxxvhypkfcigp","pxrai","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdnzxa","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvnannjxw","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrodu","kycywphmwwyeag","truu","eucgsmpsynajtisffvgqgafmdojgethmlygcekgrysvy","eucgsmpsyndddijvpxfagngnjbzxuajolf","eucgsmpsyndddijvvdpeqcwgnveozoyehjsul","eucgsmpsyndddijvsnsgoumnhjvhklzazpoqgfayum","dgnqyhduqwjunvwqkteoquyxmhi","ourbrwsthwtrfzgakvzxppbihjpsogitmoswlxalzlggzxtay","eucgsmpsyndddibedezerylnt","eucgsmpsyndddijvpxvzbiv","eucgsmpsynwdxxmogfmvuql","eucgsmpsywmnftesxvxklkezbkqbiitesnrjebsspij","eucgsbvboupistecce","iimgotnjnpwsmgqekkdtzfozjdv","eucgsmpsyndddijvpxfaxegyotcospqgyxenjferjjunmzsidt","eucgsmpsyndddijvpxfagngnjbzxuajxmvbnjxougpcblekprx","csdpcsaacavnznbqwiqlcsjzrdl","eucgsmpplakpuykrqty","eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdroje"],
"eucgsmpsyndddijvpxfagngnjbzxuajxmrmszwtjvwswgdrojjseclfhpnsjtqdqfhapmkmfqmzaunfhvkcbeqhowuuerztwldxaegwkghzthoauesdmbshzxlnpagcnyyicmtbhoqrkopemdacrkhdsxoosfhoaokqspqndtieukzjbkqixinrtqrzblufhucpzomvpmcvzfuebjfkywangcqutpzrwkwolpxuqfyjdwwrnhvnzkorsiklgqmwijynmrfezlpmdkkhafyxumiyqxhxbmxzmmcmxkajvwohhjqfuqlvknrqbjsnoimxwzbhlbddbzlwqbjpgwvjgvhgubmabuomjdmqouarvjuqzyvmsnmjaqzdmtwhaelglbt"))
'''
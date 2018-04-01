class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        ans = []
        curr, len = root, 0
        while curr:
            len += 1
            curr = curr.next
        ratio, rem = len // k, len % k
        print ratio, rem
        curr, curr_root = root, root
        for i in xrange(rem):
            if not curr:
                ans.append(curr)
                continue
            curr_root
            j = 1
            while j < ratio:
                curr = curr.next
                j += 1
            next_root = curr.next
            curr.next = None
            ans.append(curr_root)
            curr_root = next_root
        for i in xrange(rem, k):
            if not curr_root:
                ans.append(curr_root)
                continue
            j = 1
            while j < ratio - 1:
                curr = curr.next
                j += 1
            next_root = curr.next
            curr.next = None
            ans.append(curr_root)
            curr_root = next_root

        return ans

    def splitListToParts_corr(self, root, k):
        ans = []
        curr, len = root, 0
        while curr:
            len += 1
            curr = curr.next
        ratio, rem = len // k, len % k
        print ratio, rem
        curr = root
        for i in xrange(k):
            if not curr:
                ans.append(curr)
                continue
            dup = ListNode(curr.val)
            dup_root = dup
            j = 1
            cnt = ratio + 1 if i < rem else ratio
            while j < cnt:
                curr = curr.next
                dup.next = ListNode(curr.val)
                dup = dup.next
                j += 1
            ans.append(dup_root)
            curr = curr.next
        return ans
'''
class Solution_shridharsundarraj {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int numNodes = 0;
        vector<ListNode*> v;
        
        for(ListNode *f = root; f; f = f->next){
            numNodes += 1;    
        }
        
        int numAddOne = numNodes % k;
        ListNode *h = root;
        for(int i=0; i<k; ++i){
            int numHere = numNodes/k;
            if(numAddOne) {
                numHere += 1;
                numAddOne -= 1;
            }
            ListNode *newHead = new ListNode(0);
            ListNode *attach = newHead;
            while(numHere--){
                attach->next = new ListNode(h->val);
                h = h->next;
                attach = attach->next;
            }
            v.push_back(newHead->next);
            delete(newHead);
        }
        
        return v;
    }
};
'''
r1 = ListNode(1)
r1.next = ListNode(2)
r1.next.next = ListNode(3)

print Solution().splitListToParts(r1, 5)

r1 = ListNode(1)
r1.next = ListNode(2)
r1.next.next = ListNode(3)
r1.next.next.next = ListNode(4)
r1.next.next.next.next = ListNode(5)
r1.next.next.next.next.next = ListNode(6)
r1.next.next.next.next.next.next = ListNode(7)
r1.next.next.next.next.next.next.next = ListNode(8)
r1.next.next.next.next.next.next.next.next = ListNode(9)
r1.next.next.next.next.next.next.next.next.next = ListNode(10)
print Solution().splitListToParts(r1, 3)

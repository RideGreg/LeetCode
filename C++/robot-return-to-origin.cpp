// Time:  O(n)
// Space: O(1)

class Solution {
public:
    bool judgeCircle(string moves) {
        unordered_map<char, int> count;
        for (const auto& m : moves) {
            ++count[m];
        }
        return count['L'] == count['R'] && count['U'] == count['D'];
    }
};

// Time:  O(n)
// Space: O(1)
class Solution2 {
public:
    bool judgeCircle(string moves) {
        auto v = 0, h = 0;
        for (const auto& move : moves) {
            switch (move) {
                case 'U': ++v; break;
                case 'D': --v; break;
                case 'R': ++h; break;
                case 'L': --h; break;
            }
        }
        return v == 0 && h == 0;
    }
};

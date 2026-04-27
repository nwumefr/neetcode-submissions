class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_charmap;
        std::unordered_map<char, int> t_charmap;

        for(int i = 0;i<s.length();i++){
            if(s_charmap.count(s[i]) == 0){
                s_charmap[s[i]] = 0;
            }
            s_charmap[s[i]] += 1;
        }

        for(int i = 0;i<t.length();i++){
            if(t_charmap.count(t[i]) == 0){
                t_charmap[t[i]] = 0;
            }
            t_charmap[t[i]] += 1;
        }

        for(int i = 0;i<s.length();i++){
            if(t_charmap.count(s[i]) == 0){
                return false;
            }
            if(t_charmap[s[i]] != s_charmap[s[i]]){
                return false;
            }
        }
        
        return true && (s.length()==t.length());
    }
};

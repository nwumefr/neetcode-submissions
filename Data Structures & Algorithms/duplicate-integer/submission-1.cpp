#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> _map;
        for(int i = 0; i < nums.size(); i++){
            _map[nums[i]] = 0;
        }
        for(int i = 0; i < nums.size(); i++){
            _map[nums[i]] += 1;
            if(_map[nums[i]]>1){
                return true;
            }
        }
        return false;
    }
};
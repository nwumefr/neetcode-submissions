class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        _len = len(nums)
        for i in range(_len):
            _check = target - nums[i]
            if _check in nums:
                ind = nums.index(_check)
                _dict[i] = ind
        
        for i in _dict:
            if _dict[i]!=i:
                return sorted([i,_dict[i]])
        
                      
        
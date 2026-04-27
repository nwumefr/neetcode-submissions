class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        reso = []
        for i in range(len(nums)):
            mapping[i] = target - nums[i]
        for i in mapping:
            j = 0
            for k in nums:
                if k == mapping[i] and i!=j:
                    return sorted([i,j])
                else:
                    j+=1
        return [] 
        
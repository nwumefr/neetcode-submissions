class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        reso = []
        for i in range(len(nums)):
            mapping[i] = target - nums[i]
        j = 0
        reverse = {}
        for i in mapping:
            reverse[mapping[i]] = i 
        while j<len(nums):
            if reverse.get(nums[j]):
                if reverse[nums[j]]!=j:
                    if j<reverse[nums[j]]:return[j,reverse[nums[j]]]
                    return [reverse[nums[j]],j]
            j+=1
        
        return [] 
        
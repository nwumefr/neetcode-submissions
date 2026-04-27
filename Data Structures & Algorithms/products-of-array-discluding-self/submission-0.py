class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _dict = {}
        ret = []
        _len = len(nums)
        for i in range(_len):
            mult = 1
            for j in range(_len):
                if j!=i:
                    mult *= nums[j]
            ret.append(mult)
        return ret
        
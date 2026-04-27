class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _dict = {}
        for i in nums:
            if i not in _dict:
                _dict[i] = 0
            _dict[i] += 1
            if _dict[i] > 1:
                return True
        return False

        
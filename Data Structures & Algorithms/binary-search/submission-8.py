class Solution:
    def search(self, nums: List[int], target: int) -> int:
        _len = len(nums)
        newl = _len
        mid = _len//2 if _len%2 == 1 else _len//2 - 1
        if _len == 1:
            return 0 if target==nums[0] else -1
        while mid > -1 and mid < _len and target != nums[mid]:
            # find the length of the new arr we are checking
            newl = newl//2 if newl%2 == 0 else newl//2 + 1
            if target < nums[mid]:
                mid -= (newl//2 if newl%2 == 0 else newl//2 + 1)
            else:
                mid += (newl//2 if newl%2 == 0 else newl//2 + 1)
            print(newl,mid)
            if newl==1:
                print(newl)
                break  
        if mid<_len and mid>-1:
            return mid if nums[mid] == target else -1
        else:
            return -1
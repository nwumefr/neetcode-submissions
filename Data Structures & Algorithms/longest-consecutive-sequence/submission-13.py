class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # snums = sorted(nums)
        _map = {}
        _max = 1
        # print(snums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return _max
        for i in nums:
            if i not in _map:
                _map[i] = None
            if i-1 in _map:
                _map[i-1] = i
            if i+1 in _map:
                _map[i] = i+1
        print(_map)
        snums = sorted([i for i in _map])
        for i in _map:
            if not _map[i]:
                print(i)
        _j = 0
        print(snums)
        for i in range(len(snums)):
            _j+=1
            print(_max,i,snums[i])
            if snums[i] in _map and _map[snums[i]] == None:
                _max = max(_j,_max)
                _j = 0

        return _max
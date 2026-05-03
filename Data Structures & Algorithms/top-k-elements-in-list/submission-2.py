class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = {}
        for i in nums:
            if i not in _map:
                _map[i] = 0
            _map[i]+=1

        _arr = [(_map[key],key) for key in _map]
        return [i[1] for i in sorted(_arr)[::-1][:k]]
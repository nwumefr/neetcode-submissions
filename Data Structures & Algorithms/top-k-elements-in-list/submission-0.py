class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = {}
        for i in nums:
            if i not in _dict:
                _dict[i] = 0
            _dict[i] += 1
        
        rdict = {}
        for i in _dict:
            if _dict[i] not in rdict:
                rdict[_dict[i]] = []
            rdict[_dict[i]].append(i)
        
        ret = []
        for i in sorted(list(rdict.keys()))[::-1]:
            _k = 0
            for j in rdict[i]:
                ret.append(j)
            _k += len(rdict[i])
            if _k >= k:
                break
        
        return ret[:k]

        
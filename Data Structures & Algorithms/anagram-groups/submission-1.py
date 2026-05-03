class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = {}
        for i in strs:
            key = "".join(sorted(i))
            if _map.get(key) == None:
                _map[key]=[]
            _map[key].append(i)
        return [_map[i] for i in _map]
            

        
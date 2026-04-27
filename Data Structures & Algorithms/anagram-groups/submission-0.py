class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}
        for i in strs:
            default = "".join(sorted(i))
            if default not in _dict:
                _dict[default] = []
            _dict[default].append(i)
        
        return [_dict[i] for i in _dict]
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def buildTable(st:str):
            _dict = {}
            for i in st:
                if i not in _dict:
                    _dict[i] = 0
                _dict[i] += 1
            return _dict

        if buildTable(s) == buildTable(t):
            return True
        else: return False 
        
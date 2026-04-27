class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charmap: dict = {}
        charmap2: dict = {}
        
        for i in s:
            if i not in charmap:
                charmap[i] = 0
            charmap[i] += 1
        
        for i in t:
            if i not in charmap2:
                charmap2[i] = 0
            charmap2[i] += 1

        for i in charmap:
            if i not in charmap2:
                return False
            if charmap2[i] != charmap[i]:
                return False
        return True and len(s)==len(t)
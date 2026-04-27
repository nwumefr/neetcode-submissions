class Solution:
    def isPalindrome(self, s: str) -> bool:
        _len = len(s)
        i = 0
        j = _len - 1
        while i!=_len-1 and j!=0 and i<j:
            while not s[i].isalnum() and i!=_len-1:
                i+=1
            while not s[j].isalnum() and j!=0:
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
            i+=1
            j-=1
        return True
        
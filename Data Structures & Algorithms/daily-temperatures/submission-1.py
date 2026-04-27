class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ith = 0
        ret = []
        _len = len(temperatures)
        for i in range(_len):
            if i==_len-1:
                ret.append(0)
                continue
            warmer = i+1
            count = 0
            while warmer<_len and temperatures[i]>=temperatures[warmer]:
                warmer+=1
                count+=1
            if warmer>=_len:
                ret.append(0)
            else:
                ret.append(warmer-i)
        
        return ret
        
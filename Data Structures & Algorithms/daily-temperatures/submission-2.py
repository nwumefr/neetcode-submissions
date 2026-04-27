class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ith = 0
        ret = []
        _len = len(temperatures)
        for i in range(_len):
            # if the last temp default to 0
            if i==_len-1:
                ret.append(0)
                continue
            # start of warmer count index
            warmer = i+1
            while warmer<_len and temperatures[i]>=temperatures[warmer]:
                # count until we find a temp greater than temp[i]
                warmer+=1
            if warmer>=_len:
                # if warmer index is greater than or equal to _len then we hit the array boundary
                # so there isnt actually anything warmer past that
                # and we default to zero 
                ret.append(0)
            else:
                # otherwise, the count is the warmer index - the actual index
                ret.append(warmer-i)
        
        return ret
        
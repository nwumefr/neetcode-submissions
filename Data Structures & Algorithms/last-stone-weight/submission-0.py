class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = stones
        while len(a)>2:
            max1 = max(a)
            a.remove(max1)
            max2 = max(a)
            a.remove(max2)
            val = abs(max1-max2)
            if val>0:
                a.append(val)
        
        if len(a) == 1:
            return a[0]
        elif len(a) == 2:
            return abs(a[0]-a[1])
        else:
            return 0

        
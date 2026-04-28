class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in strs:
            for c in i:
                order = ord(c)
                # if order>15:
                #     encoded+='0'
                encoded+=hex(order)
            encoded+='-'
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        _idx = 0
        for i in s.split("-")[:-1]:
            st = ''
            buffer_start = 0
            for k in range(len(i)):
                # print(k)
                if (k+1)%4 == 0:
                    st+=chr(int(i[buffer_start:k+1],16))
                buffer_start = k
            res.append(st)
        
        return res

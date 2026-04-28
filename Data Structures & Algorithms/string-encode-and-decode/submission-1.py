class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in strs:
            for c in i:
                order = ord(c)
                # if order>15:
                #     encoded+='0'
                encoded+=hex(order)
            encoded+=hex(128)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        _idx = 0
        buffer = ''
        hex_buffer = ''
        for i in range(len(s)):
            hex_buffer += s[i]
            if (i+1)%4 == 0:
                order = int(hex_buffer,16)
                if order>127:
                    res.append(buffer)
                    buffer = ''
                else:
                    buffer+=chr(order)
                hex_buffer = ''       
        
        return res

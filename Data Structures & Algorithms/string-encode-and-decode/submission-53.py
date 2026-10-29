import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            leng = len(s)
            encoded += str(leng) + "|" + s
        #print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        hold = ""
        i = 0
        n = len(s)
        while i < n:
            delim = s.find("|", i)
            length = int(s[i:delim])
            decoded.append(s[delim + 1 : delim + 1 + length])
            i = delim + 1 + length
        return decoded

            
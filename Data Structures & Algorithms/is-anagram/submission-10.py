class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictT,dicts = {},{}

        for i in range(0,len(s)):
            dicts[s[i]] = 1+ dicts.get(s[i],0)
            dictT[t[i]] = 1 + dictT.get(t[i],0)
        return dicts == dictT
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {},{}
        if len(s) != len(t):
            return False

        for x in range(len(s)):
            dictS[s[x]] = 1 + dictS.get(s[x],0)
            dictT[t[x]] = 1 + dictT.get(t[x],0)
            
        return dictS == dictT
    



        
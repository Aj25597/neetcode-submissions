class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            ")" :"(",
            "}": "{",
            "]" : "["
        }
        staack = []
        for cha in s:
            if cha in valids.values():
                #Indicates Key, push
                staack.append(cha)
            else:
                try:
                    popped = staack.pop()
                except:
                    return False
                #Grab value associated with value 
                if valids[cha] != popped:
                    return False
        return True if len(staack) == 0 else False
        
        

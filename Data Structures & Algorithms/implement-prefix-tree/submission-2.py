class PrefixTree:

    #Root = {a: {p: {p: {l: e: {'END',s: {'END'}} }}}}

    def __init__(self):
        #26 unique characters
        self.root = {}

    def insert(self, word: str) -> None:
        #Start self root,
        curr = self.root
        for x in word:
            if x in curr.keys():
                #Don't need to insert
                curr = curr[x]
                #Return a dictionary
            else:
                curr[x] = {}
                curr = curr[x]
        #Technically, curr should point to last dictionary
        curr["END"] = True
    
    def search(self, word: str) -> bool:
        curr = self.root #Dictionary
        for x in word:
            if x in curr.keys():
                curr = curr[x]
            else:
                return False
        return True if "END" in curr.keys() else False


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for x in prefix:
            if x in curr.keys():
                curr = curr[x]
            else:
                return False
        return True        
        
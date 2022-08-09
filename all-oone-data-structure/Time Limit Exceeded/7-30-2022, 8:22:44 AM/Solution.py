// https://leetcode.com/problems/all-oone-data-structure

class AllOne:

    def __init__(self):
        self.d = {}

    def inc(self, key: str) -> None:
        if key in self.d:
            self.d[key] +=1
        else:
            self.d[key] = 1
        return None

    def dec(self, key: str) -> None:
        if key not in self.d:
            return
        else:
            if self.d[key] >1: 
                self.d[key] -= 1
            elif self.d[key] == 1:
                del self.d[key]

    def getMaxKey(self) -> str:
        if len(self.d) == 0:
            return ""
        
        return max(self.d, key=self.d.get)

    def getMinKey(self) -> str:
        if len(self.d) == 0:
            return ""
        return min(self.d, key=self.d.get)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
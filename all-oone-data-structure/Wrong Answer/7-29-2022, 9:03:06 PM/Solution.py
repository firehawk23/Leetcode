// https://leetcode.com/problems/all-oone-data-structure

class AllOne:

    def __init__(self):
        self.d = dict()

    def inc(self, key: str) -> None:
        if key in self.d:
            self.d[key] +=1
        else:
            self.d[key] = 1
        return None

    def dec(self, key: str) -> None:
        if self.d[key] == 0:
            del self.d[key]
        else:
            self.d[key] -= 1

    def getMaxKey(self) -> str:
        if self.d == {}:
            return ""
        return max(self.d, key= lambda x: self.d[x])

    def getMinKey(self) -> str:
        if self.d == {}:
            return ""
        return min(self.d, key= lambda x: self.d[x])


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
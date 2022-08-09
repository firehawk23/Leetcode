// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.append(-1)
        for i in range(1,len(arr)):
            arr[i-1] = max(arr[i:])
        arr.remove(-1)
        return arr
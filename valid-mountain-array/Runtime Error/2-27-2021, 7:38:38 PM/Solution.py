// https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr)<3):
            return False
        c = False
        for i in range(1,len(arr)):
            if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
                c = not(c)
        return c
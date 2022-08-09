// https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False
        else:
            m = x = 1
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i + 1] and m == 1:
                    m = 1
                elif arr[i] > arr[i + 1]:
                    m = 0
                else:
                    x = 2
            return True if m == 0 and x == 1 else False
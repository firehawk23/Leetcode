// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        num = 1
        while num**2 <= x:
            low = num
            num *= 2

        high = num
        while low <= high:
            mid = low + (high - low)//2
            squared = mid**2
            if squared == x:
                return mid
            elif squared < x:
                low = mid + 1
            else:
                high = mid - 1

        return high

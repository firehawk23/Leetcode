// https://leetcode.com/problems/4sum-ii

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n12,ans = defaultdict(int),0
        for i in nums1:
            for j in nums2:
                n12[i+j]+=1
        for k in nums3:
            for l in nums4:
                ans+=n12[-(k+l)]
        return ans
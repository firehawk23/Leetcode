// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left,right;
        left = Solution::BS(nums,target,true);
        right = Solution::BS(nums,target,false);
        vector<int> res{left,right};
        return res;
    }
    
    int BS(vector<int>& nums, int target, bool leftbias){
        int r,l,mid,i;
        r= nums.size()-1;
        l = 0;
        i=-1;
        while(l<=r){
            mid = (int)(l+r)/2;
            if(target>nums[mid]){
                l = mid+1;
            }
            else if(target<nums[mid]){
                r = mid-1;
            }
            else{
                i=mid;
                if(leftbias){
                    r= mid-1;
                }
                else{
                    l= mid+1;
                }
            }
        }
    
        return i;
    }
};


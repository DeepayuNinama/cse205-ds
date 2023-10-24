from ast import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in nums:
            
        #0 <= i < nums.length    
            ans[i] = nums[nums[i]]
        return ans  
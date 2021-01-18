from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [i for i in range(len(nums))]
        dp[0]=nums[0]
        max_=dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(0,dp[i-1])+nums[i]
            max_ = max(dp[i],max_)
        return max_

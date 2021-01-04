from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0 for i in range(len(nums)+1)]
        dp[0] = 0
        max_nums = nums[0]
        for i in range(1,len(nums)+1):
            dp[i] = nums[i-1]+dp[i-1] if dp[i-1]>0 else nums[i-1]
            max_nums = max(dp[i],max_nums)
        return max_nums

if __name__=="__main__":
    solution = Solution()
    solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
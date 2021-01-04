class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        max_nums = max(dp[0], dp[1])

        for i in range(len(nums)):
            for j in range(i - 2, -1, -1):
                dp[i] = max(dp[j] + nums[i], dp[i])
            max_nums = max(dp[i], max_nums)
        return max_nums
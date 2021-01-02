from typing import List
class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k!=0 and len(nums)!=1 and len(nums)!=0:
            if k>len(nums):
                k = k%len(nums)
            k_list = nums[-k:]
            nums[k:] = nums[:len(nums)-k]
            nums[0:k] = k_list
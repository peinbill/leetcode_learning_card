from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count=0
        for i in nums:
            if i>target:
                break
            if i==target:
                count+=1
        return count

    def search2(self, nums: List[int], target: int) -> int:
        count=0
        start = 0
        end = len(nums)-1
        token_find = False
        while start<= end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                token_find = True
                break
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1

        if token_find:
            pre = mid-1
            post = mid+1
            # 往前找
            while pre>=0 and nums[pre]==target:
                count+=1
                pre -= 1
            # 往后找
            while post<len(nums) and nums[post]==target:
                count+=1
                post+=1
        return count
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)-1
        def search(i,target)->int:
            start = 0
            while start<= end:
                mid = start+(end-start)//2
                if target==nums[mid]:
                    return mid
                elif target>nums[mid]:
                    start=mid+1
                else:
                    end = mid-1
            return -1

        result = []
        for index,i in enumerate(nums):
            if i>target:
                break
            back = target-i
            return_index = search(index+1,back)
            if return_index==-1:
                continue
            result.append(i)
            result.append(nums[index+1+return_index])
            break
        return result

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        result = []
        map_list = dict()
        for i in nums:
            map_list[i]=i
        for i in nums:
            if i>target:
                break
            if target-i in map_list:
                result.append(i)
                result.append(target-i)
                break
        return result

    def twoSum3(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [nums[l], nums[r]]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []



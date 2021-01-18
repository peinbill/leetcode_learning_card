from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k-1
        result = []
        if len(nums)==0:
            return result
        while end<=len(nums)-1:
            tmp_result = max([nums[i] for i in range(start,end+1)])
            result.append(tmp_result)
            start+=1
            end+=1
        return  result


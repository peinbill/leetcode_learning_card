from typing import List
class Solution26:
    def removeDuplicates(self, nums:List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        i = 0
        while True:
            if i + 1 >= len(nums):
                break
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
                continue

        return len(nums)

if __name__=="__main__":
    solution26 = Solution26()
    print(solution26.removeDuplicates([1,1,2]))
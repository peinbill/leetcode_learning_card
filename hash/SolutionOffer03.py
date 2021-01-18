class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        count = dict()
        for i in nums:
            if i in count:
                return i
            else:
                count[i] = i
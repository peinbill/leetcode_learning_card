from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = []
        non_odd = []
        for num in nums:
            if num%2==0:
                non_odd.append(num)
            else:
                odd.append(num)
        return odd+non_odd


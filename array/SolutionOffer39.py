from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = dict()
        for i in nums:
            map[i]=map.get(i,0)+1
        threhold = len(nums)//2
        for key,value in map.items():
            if value>threhold:
                return key

if __name__=="__main__":
    solution = Solution()
    print(solution.majorityElement([[1, 2, 3, 2, 2, 2, 5, 4, 2]]))
from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        start = 0
        end = len(numbers)-1

        while (start+1<end):
            if numbers[start]<numbers[end]:
                return numbers[start]

            mid = start+(end-start)//2
            if numbers[mid]>numbers[start]:
                start = mid
            elif numbers[mid]<numbers[start]:
                end = mid
            else:
                start += 1

        if(numbers[start]<numbers[end]):
            return numbers[start]
        else:
            return numbers[end]


from typing import List
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        last = 10**n
        return [i for i in range(1,last)]
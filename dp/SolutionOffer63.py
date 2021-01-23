from typing import List
from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        min_price = prices[0]
        dp=[0 for i in prices]
        dp[0]=0
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1],prices[i]-min_price)
            min_price=min(prices[i],min_price)
        return dp[-1]
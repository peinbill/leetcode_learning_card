from typing import List

class Solution122:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        is_buy = False
        buy_price = 0
        for i in range(1,len(prices)):
            # 先买入
            if not(is_buy) and prices[i-1]<prices[i]:
                is_buy = True
                buy_price = prices[i-1]
            # 卖出
            if is_buy and prices[i-1]>prices[i]:
                is_buy = False
                sum += prices[i-1]-buy_price
            # 卖出的另一种特殊情况——价格一直在上升，但是此时已经是最后一天
            if is_buy and i==len(prices)-1 and buy_price<= prices[i]:
                sum += prices[i]-buy_price

        return sum
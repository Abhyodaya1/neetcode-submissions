class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,len(prices)-1
        min_buy,profit=float('inf'),0
        for price in prices:
            min_buy = min(min_buy,price)
            if price>min_buy:
                profit= max(profit,price-min_buy)
            
        return profit

        
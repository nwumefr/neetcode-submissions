class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        _len = len(prices)
        for i in range(_len):
            nmax = max(prices[i:])
            print(prices[i],nmax,nmax-prices[i])
            profit = max(profit,nmax-prices[i])
        return profit
            
                
        
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s_pr = 0
        for i in range(len(prices) - 1):
            pr = prices[i+1] - prices[i]  
            if pr >= 0:
                s_pr += pr
        return s_pr
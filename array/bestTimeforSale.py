class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l,r=0,1 #L =buying, r=selling
        maxPrice=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxPrice=max(maxPrice,profit)
            else:
                l=r #move left to right because buying prices 
                    #because bp has to be lower than sp
            r+=1

        return maxPrice
# Time complexity= O(N)
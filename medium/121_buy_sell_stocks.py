# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

def maxProfit(self, prices):
        if len(prices) == 0: return 0
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        
        return maxProfit

#  Track the maxProfit and minPrice.

#  Iterate through the array. Assume the first ele is the min price. If the next ele is lower than the min price, replace min price. 

#  If the next ele - the min price is larger than the maxProfit, replace the maxProfit. Return the maxProfit at the end.


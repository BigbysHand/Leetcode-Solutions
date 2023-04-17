class Solution(object):
    def maxProfit(self, prices):
        #O(n) max diff finder
        min = prices[0]
        diff = 0
        for idx in prices[1:]:
            if idx < min:
                min = idx
            tmp = idx = min
            if tmp > diff:
                diff = tmp
        return diff
            


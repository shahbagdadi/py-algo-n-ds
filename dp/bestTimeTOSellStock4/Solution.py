from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #The problem is hard
        #Time complexity, O(nk)
        #Space complexity, O(nk)
        length = len(prices)
        if length < 2:
            return 0
        max_profit = 0
        #if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
        if k>=length/2:
            for i in range(1,length):
                max_profit += max(prices[i]-prices[i-1],0)
            return max_profit
        
        #max_global[i][j] is to store the maximum profit, at day j, and having i transactions already
        #max_local[i][j] is to store the maximum profit at day j, having i transactions already, and having transaction at day j
        max_global = [[0]*length for _ in range(k+1)]
        max_local = [[0]*length for _ in range(k+1)]

        #i indicates the transaction times, j indicates the times
        for j in range(1,length):
            cur_profit = prices[j]-prices[j-1] #variable introduced by the current day transaction
            for i in range(1,k+1):
                #max_global depends on max_local, so updata local first, and then global.
                max_local[i][j] = max( max_global[i-1][j-1]+max(cur_profit,0), max_local[i][j-1] + cur_profit)
                #if cur_profit <0, then the current transaction loses money, so max_local[i][j] = max_global[i-1][j-1]
                #else, it can be max_global[i-1][j-1] + cur_profit, by considering the current transaction
                #or it can be max_local[i][j-1] + cur_profit, this is to CANCEL the last day transaction and moves to the current transaction. Note this doesn't change the total number of transactions. Also, max_local[i-1] has already been considered by max_global[i-1] term
                max_global[i][j] = max(max_global[i][j-1], max_local[i][j])
                #This is more obvious, by looking at whether transaction on day j has influenced max_global or not. 
        return max_global[k][-1] #the last day, the last transaction

s = Solution()
ip = [3,2,6,5,0,3]
ans = s.maxProfit(2,ip)
print(ans)
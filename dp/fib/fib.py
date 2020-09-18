from functools import lru_cache

class Solution :

    # T - O(2^n)   S - O(n)
    def fib(self,n:int) :
        if n <= 1 :
            return n
        return self.fib(n-1) + self.fib(n-2)

    # T - O(n) S - O(n)
    def fibMemo(self , n :int) :
        lookup = [0] * (n+1)
        def helper(n,lookup) :
            if n <=1 :
                return n
            if lookup[n] != 0 :
                return lookup[n]
            lookup[n] = helper(n-1,lookup) + helper(n-2,lookup)
            return lookup[n]
        return helper(n,lookup)

    # T - O(n) S - O(n)
    @lru_cache
    def fibLRU(self,n:int) :
        if n <= 1 :
            return n
        return self.fib(n-1) + self.fib(n-2)

    # T - O(n) S - O(n) 
    def fibDP(self,n:int) :
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,len(dp)) :
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


s = Solution()
ans = s.fib(5)
print(ans)

ans1 = s.fibMemo(5)
print(ans1)

ans2 = s.fibLRU(5)
print(ans2)

ans3 = s.fibDP(5)
print(ans3)
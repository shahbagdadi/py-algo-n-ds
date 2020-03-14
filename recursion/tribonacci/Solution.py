class Solution:
    # T - O(3^n)  S - O(n)
    def tribonacciR(self, n: int) -> int:
        if n <= 0 :
            return 0
        elif n == 1 :
            return 1
        return self.tribonacciR(n-3) + self.tribonacciR(n-2) + self.tribonacciR(n-1) 

    # T - O(n)   S - O(1)
    def tribonacci(self, n: int) -> int:
        a, b, c = 1,0,0
        for _ in range(n) :
            a, b, c = b , c, a + b + c
        return c

s = Solution()
print(s.tribonacci(25))
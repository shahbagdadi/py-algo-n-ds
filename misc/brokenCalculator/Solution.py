

class Solution:
    # Explanation - https://leetcode.com/problems/broken-calculator/discuss/236565/Detailed-Proof-Of-Correctness-Greedy-Algorithm
    def brokenCalc(self, X: int, Y: int) -> int:
        cnt = 0
        while Y != X:
            if X > Y : return cnt + X - Y
            # if y is even last move for min was multiplication
            if Y % 2 == 0 : 
                Y = Y // 2
            else:   # for Y odd the last move has to be from Y+1
                Y += 1
            cnt += 1
        return cnt


s = Solution()
print(s.brokenCalc(3,10))
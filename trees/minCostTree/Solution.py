from typing import List


class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        '''
             24            24
            /  \          /  \
            12   4        6    8
            /  \               / \
            6    2             2   4

            for arr = [6,2,4] keep iterating array till you find a number greater than its previous
            then the previous (2) can for a tree with its previous (6) or the current (4)
            Always choose the smaller and make the tree so
            sum = 2 * min(4,6) = 8 
        '''
        res = 0
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                r = mid * min(stack[-1], a)
                print(r)
                res += r
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
        
s = Solution()
print(s.mctFromLeafValues([6,2,1,4,5]))
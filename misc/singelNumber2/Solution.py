from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones , twos, threes = 0 ,  0, 0
        for n in nums:
            twos |= (ones & n)
            ones ^= n
            threes = ones & twos
            ones &= ~threes # remove the threes from the ones
            twos &= ~threes # remove the threes from the twos
            print(f'{ones} , {twos}, {threes}')
        return ones

s = Solution()
ip = [1,1,1,2]
ans = s.singleNumber(ip)
print(ans)
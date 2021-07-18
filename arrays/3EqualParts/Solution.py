from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:  
        ones = [i for i, num in enumerate(arr) if num == 1]
        l = len(ones) # number of ones
        if l % 3 != 0: 
            return [-1, -1]  # if number of 1's not divisible by 3 then it caanot be split into 3 parts
        elif l == 0:
            return [0, len(arr) - 1] # if 0 1's you can split anyway so 0,last
        ending_zeros = len(arr) - ones[-1] - 1 # length of array - last 1 -1
        i1 = ones[l // 3 - 1] + ending_zeros
        i2 = ones[2 * l // 3 - 1] + 1 + ending_zeros
        if arr[ones[0]:i1 + 1] == arr[ones[l // 3]:i2] == arr[ones[2 * l // 3]:]:
            return [i1, i2]
        return [-1, -1]

s = Solution()
ip = [1,1,0,0,0,1,1,0,0,0,1,1,0]
ans = s.threeEqualParts(ip)
print(ans)
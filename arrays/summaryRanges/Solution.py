from typing import List

class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        i,j,L , ans = 0 , 0, len(nums)-1, []

        def range(l,r):
            return str(l) if l == r else f'{l}->{r}'

        while j < L :
            if nums[j] +1 != nums[j+1]:
                ans.append(range(nums[i],nums[j]))
                i = j +1
            j += 1
        ans.append(range(nums[i],nums[j]))
        return ans
            



s= Solution()
ip = [0,3,4,5,7]
# ip = [0,2,3,4,6,8,9]
# ip = [1,3]
ans = s.summaryRanges(ip)
print(ans)

class Solution:

    def subsets(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                # if i > start and nums[i] == nums[i-1]: continue  # if dups in nums
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        # nums.sort()                                               # if dups in nums
        backtrack(0, len(nums), [])
        return ans

    # same as subsets above
    def combinations(self,l):    
        if l == []: return [[]]    
        return self.combinations(l[1:]) + [[l[0]] + c for c in self.combinations(l[1:])]

    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]       
        ans = []
        backtrack(0, len(nums))
        return ans



ip = [1,2,3]
s = Solution()
sets = s.subsets(ip)
print(f'Powerset => {sets}')
# same as above
comb = s.combinations(ip)
print(f'Powerset2 => {comb}')


perm = s.permute(ip)
print(f'Permutation => {perm}')




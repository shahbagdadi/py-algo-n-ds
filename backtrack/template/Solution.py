
class Solution:

    def subsets(self, A):
        def backtrack(s, e, tmp):
            ans.append(tmp[:])
            for i in range(s, e):
                # if i > start and nums[i] == nums[i-1]: continue  # if dups in nums
                tmp.append(A[i])
                backtrack(i+1, e, tmp)
                tmp.pop()
        ans = []
        # nums.sort()                                               # if dups in nums
        backtrack(0, len(A), [])
        return ans

    # same as subsets above
    def combinations(self,l):    
        if l == []: return [[]]    
        return self.combinations(l[1:]) + [[l[0]] + c for c in self.combinations(l[1:])]

    def permute(self, A):
        def backtrack(s, e):
            if s == e:
                ans.append(A[:])
            for i in range(s, e):
                A[s], A[i] = A[i], A[s]
                backtrack(s+1, e)
                A[s], A[i] = A[i], A[s]       
        ans = []
        backtrack(0, len(A))
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




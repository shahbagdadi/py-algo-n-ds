class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ctr = { c for c in J}
        ans =0
        for c in S:
            if c in ctr:
                ans +=  1
        return ans

    def numJewelsInStones1(self, J, S):
        return sum(map(S.count, J))   

    def numJewelsInStones2(self, J, S):
        return sum(s in J for s in S)

s = Solution()
print(s.numJewelsInStones('aA', 'aAAbbbb'))
print(s.numJewelsInStones1('aA', 'aAAbbbb'))
print(s.numJewelsInStones2('aA', 'aAAbbbb'))
class Solution(object):
    def countSubstrings(self, S):
        #Explanation - https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)/115920
        ans = 0
        for i in range(len(S)):
            for j in range(2):
                left = i
                right = left + j

                while left >= 0 and right < len(S) and S[left] == S[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans

s = Solution()
ip = 'aaa'
ans = s.countSubstrings(ip)
print(ans)
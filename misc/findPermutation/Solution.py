from typing import List

class Solution:
    #make an increasing array of range [1, N] and if we face any "D" character we reverse sequence for consecutive "D"
    def findPermutation(self, s: str) -> List[int]:
        arr , cnt , n = list(range(1,len(s)+2)), 0 , len(s)
        for i in range(n+1):
            if i < n and s[i] == 'D' :
                cnt += 1 
            else :
                arr[i - cnt : i+1] = arr[i - cnt : i+1] [::-1]
                cnt = 0
        return arr

s = Solution()
ip = 'IDDIDDDI'
ans = s.findPermutation(ip)
print(ans)
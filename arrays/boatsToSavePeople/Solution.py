from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i , j , ans = 0, len(people)-1, 0
        while i < j :
            if people[i] + people[j] <= limit :
                j -= 1
            ans += 1
            i += 1
        return ans+1
            
s = Solution()
ip = [3,5,3,4]
ans = s.numRescueBoats(ip,5)
print(ans)
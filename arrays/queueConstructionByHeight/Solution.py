from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0],x[1]))
        ans = []
        for p in people:
            ans.insert(p[1],p)
        return ans
        
s = Solution()
ip = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
ans = s.reconstructQueue(ip)
print(ans)
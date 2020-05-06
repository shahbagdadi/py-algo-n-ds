from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s,e]] +  right



s = Solution()
# # ip1 = [[1,3],[6,9]]
# # ip2 = [2,5]
ip1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
ip2 = [4,8]
# ip1 = [[1,5]]
# ip2 = [6,8]
ans = s.insert(ip1, ip2)
print(ans)

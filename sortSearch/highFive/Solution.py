from typing import List
import collections
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores , res = collections.defaultdict(list), []
        for i in items:
            s = scores[i[0]]
            if len(s) == 5:
                heapq.heappushpop(s,i[1])
            else:
                heapq.heappush(s,i[1])
        for c in scores :
            avg = sum(scores[c]) // len(scores[c])
            res.append([c, avg])
        return res

        

s = Solution()
ip = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
ans = s.highFive(ip)
print(ans)
        
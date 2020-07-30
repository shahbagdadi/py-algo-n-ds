from typing import List
import heapq

class Solution:
    def KListSort(self,KList : List[List]) -> List:
        data , result = [], []
        for i in range(len(KList)):
            if KList[i] :
                heapq.heappush(data,(KList[i][0],i,0))
        while data :
            val, i, j = heapq.heappop(data)
            result.append(val)
            if  j+1 < len(KList[i]):
                heapq.heappush(data,(KList[i][j+1],i, j+1))
        return result


s = Solution()
ip = [[2,4,6,8],
[3,5,7,12],
[9,10,13],
[1]]
ans = s.KListSort(ip)
print(ans)
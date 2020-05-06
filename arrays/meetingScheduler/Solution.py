from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i,j,N,M,ans = 0,0,len(slots1), len(slots2), []
        slots1.sort(key= lambda x: x[0])
        slots2.sort(key= lambda x: x[0])
        while i < N and j < M :
            if slots1[i][1] < slots2[j][0] :
                i += 1
            elif slots2[j][1] < slots1[i][0] :
                j += 1
            else:
                s = max(slots1[i][0], slots2[j][0])
                e = min(slots1[i][1], slots2[j][1])
                if e - s >= duration :
                    return [s, s + duration ] 
                elif slots1[i][1] < slots2[j][1]:
                    i += 1
                else:
                    j += 1
        return[ ]



s = Solution()
ip1 = [[10,50],[60,120],[140,210]]
ip2 = [[0,15],[60,70]]
duration = 8
ans = s.minAvailableDuration(ip1, ip2, duration)
print(ans)

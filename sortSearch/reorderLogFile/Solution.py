from typing import List
import sys

class Solution:
    def reorderLogFiles1(self, logs: List[str]) -> List[str]:
        dlog , llog = [] , []
        for log in logs:
            i,t,*rl = log.split()
            if t.isdigit() :
                dlog.append((t,rl, log))
            else :
                llog.append((t,rl, log))
        llog.sort()
        return [ log[2] for log in llog + dlog]
            
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(log):
            i,t,*rl = log.split()
            if t.isdigit() :
                return (1,)
            else:
                return (0,t,rl,log)
        return sorted(logs, key=custom_sort)


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

s = Solution()
ans = s.reorderLogFiles(logs)
print(ans)
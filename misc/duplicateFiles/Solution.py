from typing import List
import collections
import re


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fdict = collections.defaultdict(list)

        def folder(rec):
            d, *files = rec.split()
            for f in files:
                ftuple = re.findall(r'([\w\.]+)', f)
                fdict[ftuple[1]].append(d + '/' + ftuple[0])

        for path in paths:
            folder(path)
        return [v for v in fdict.values() if len(v) > 1]


s = Solution()
ip = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
      "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
ans = s.findDuplicate(ip)
print(ans)

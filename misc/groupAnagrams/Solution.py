from typing import List
import collections
import itertools


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        da = collections.defaultdict(list)
        for w in strs:
            k = str(sorted(w))
            da[k].append(w)
        return list(da.values())

    def oneLiner(self, strs: List[str]) -> List[List[str]]:
        print(sorted(strs, key=sorted))
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.oneLiner(["eat", "tea", "tan", "ate", "nat", "bat"]))

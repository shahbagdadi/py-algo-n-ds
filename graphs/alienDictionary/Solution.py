from typing import List
import collections

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        degree = {key: 0 for key in set(''.join(words))}
        graph = collections.defaultdict(list)

        # build graph for topological sort
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1,w2):
                if c1 != c2:
                    degree[c2] += 1
                    graph[c1].append(c2)
                    break
            else:
                if len(w1) > len(w2): return ""

        lst_no_dep = [ x for x in degree.keys() if degree[x] == 0]

        # Topological sort
        stk = []
        while lst_no_dep:
            ch = lst_no_dep.pop()
            stk.append(ch)
            for ch_greater in graph[ch]:
                degree[ch_greater] -= 1
                if degree[ch_greater] == 0:
                    lst_no_dep.append(ch_greater)

        return ''.join(stk) if len(stk) == len(degree) else ''

s = Solution()
ip = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
ans = s.alienOrder(ip)
print(ans)
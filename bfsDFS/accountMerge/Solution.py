from typing import List
import heapq
from collections import defaultdict


class Account:
    def __init__(self, l):
        self.name = l[0]
        self.emails = l[1:]

    # needed for set operations
    def __hash__(self):
        return hash(str(self))

    # needed for set operations
    def __eq__(self, other):
        return self.name == other.name and len(self.emails) == len(other.emails) \
               and set(self.emails) == set(other.emails)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [Account(a) for a in accounts]
        email_dict, visited, finalres = defaultdict(set), set(), []

        for acc in accounts:
            for email in acc.emails:
                email_dict[email].add(acc)

        for acc in accounts:
            if acc in visited: continue
            res = set()
            self.dfs(acc, email_dict, visited, res)
            finalres.append([acc.name] + sorted(res))
        return finalres
    
    def dfs(self, acc, email_dict, visited, res):
        if acc in visited: return
        visited.add(acc)
        for email in acc.emails:
            res.add(email)
            for a in email_dict[email]:
                self.dfs(a, email_dict, visited, res)

s = Solution()
ip = [["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]]
ans = s.accountsMerge(ip)
print(ans)
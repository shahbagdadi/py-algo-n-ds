from typing import List
from functools import lru_cache
import collections
import math
import itertools

class Solution:

    def minTransfers(self, transactions: List[List[int]]) -> int:
        tuplify = lambda balance: tuple(sorted((k, v) for k, v in balance.items()))  # create a tuple from the dict so we can use lru_cache

        @lru_cache(None)
        def dfs(balances):
            # print(balances)
            if not balances:
                return 0            #return 0 if all settled
            res = math.inf
            balances = {k: v for k, v in balances}
            print(balances)
            for size in range(2, len(balances) + 1):
                for group in itertools.combinations(balances.keys(), size):     # try all combination to balance the debts starting with 2 combinations
                    print(group)
                    if sum(balances[k] for k in group) == 0:
                        remaining_balances = {k: v for k, v in balances.items() if k not in group}      # if you can balance , then get rid of them frm balances
                        res = min(res, size - 1 + dfs(tuplify(remaining_balances)))  # trx to settle in this group + dfs(remaining) 
            return res

        balances = collections.defaultdict(int)     #manage the debt for each person
        for u, v, z in transactions:
            balances[u] += z
            balances[v] -= z
        print(balances)
        return dfs(tuplify({k: v for k, v in balances.items() if v}))


s = Solution()
trx = [[0,1,10], [1,0,1], [1,2,5], [2,0,5],[3,0,7]]
ans = s.minTransfers(trx)
print(ans)
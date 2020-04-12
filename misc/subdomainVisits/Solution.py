from typing import List
from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for site in cpdomains:
            count,domain = site.split(' ')
            cnt = int(count)
            sub_domain = domain.split('.')
            d = ''
            for sd in reversed(sub_domain):
                d = sd + '.' + d
                counter[d] += cnt
        return [ str(v) + ' ' + k[:-1] for k,v in counter.items()]
        

s = Solution()
ip = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(s.subdomainVisits(ip))


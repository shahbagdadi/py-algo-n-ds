from typing import List
import collections

class Solution:
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        prev_list,ans,prev_freq = [] , [] , 0
        print(counter)
        for word,freq in counter.most_common():
            if prev_freq == freq:
                prev_list.append(word)
            else:
                prev_list.sort()
                if prev_list : ans += prev_list[:k-len(ans)]
                prev_list , prev_freq = [word] , freq
        if len(ans) < k : 
            prev_list.sort()
            ans += prev_list[:k-len(ans)]
        return ans

    def topKFrequent(self, words, k):
        d = collections.Counter(words)
        ans = sorted(d.keys(), key=lambda word: (-d[word], word))
        return ans[:k]



s = Solution()
# ip = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
# ip = ["i", "love", "leetcode", "i", "love", "coding"]
ip = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
ans = s.topKFrequent(ip,4)
print(ans)

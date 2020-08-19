from typing import List

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set('aeiouAEIOU')
        words = S.split()
        for i in range(len(words)):
            w = words[i]
            if w[0] not in vowels :
                w = w[1:] + w[0]
            w += 'ma' + 'a' * (i+1)
            words[i] = w
        return ' '.join(words)



s = Solution()
ip = 'I speak Goat Latin'
ans = s.toGoatLatin(ip)
print(ans)
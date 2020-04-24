
class Solution:
    def reorganizeString(self, S):
        ss = sorted(S)                  # sort the string
        ssl = sorted(ss, key=S.count)   # sort the sorted string now by length such the highest freq at end
        # print(ssl)
        mid = len(ssl) // 2
        ssl[1::2], ssl[::2] = ssl[:mid], ssl[mid:]  # interlace the first half and send half of the array using step =2
        return ''.join(ssl) if ssl[-1:] != ssl[-2:-1] else ''   # if last and second last is same then return ''

s = Solution()
print(s.reorganizeString('aadahbb'))
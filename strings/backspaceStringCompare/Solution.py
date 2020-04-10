import itertools

class Solution:
    # T - O(m + n)   S - O(m+n)
    def backspaceCompare(self, S: str, T: str) -> bool:
        def strim(S):
            skip, ans = 0, []
            for c in reversed(S):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    ans.append(c)
            return str(ans)
        return strim(S) == strim(T)

    # T - O(m + n)   S - O(m+n)
    def bc(self, S: str, T: str) -> bool:
        def strim(S):
            skip = 0
            for c in reversed(S):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c
        return all( x == y for x,y in itertools.zip_longest(strim(S),strim(T)))


s = Solution()
print(s.backspaceCompare('ab##', 'c#d#'))
print(s.bc('ab##', 'c#d#'))



class Solution:
    def kthGrammar1(self, N: int, K: int) -> int:
        """ T - O(N * 2 ^N)   & S - O(2^N) """
        l = [0]
        for i in range(N-1):
            l += [ n^1 for n in l]
        print(l)
        return l[K-1]

    def kthGrammar(self, N: int, K: int) -> int:
        """ T - O(1) S - O(1)
        https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/113705/JAVA-one-line/114739
        """
        return bin(K - 1).count('1') & 1

s = Solution()
print(s.kthGrammar(4,2))

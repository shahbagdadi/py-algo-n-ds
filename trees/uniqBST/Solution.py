class Solution:
    def numTrees(self, N : int) -> int:
        '''
            For an array [1,2,3,4,5] the number of BST's we can form at each node say '3' is the
            the number of BST that can be formed with permutation of [1,2] on the left and [4,5] on the right
            So if we follow the same logic for each i in the array we should get the total count.
            F(i,n) -> Number of BST at i given an array of n numbers
            F(i,n) = G(i-1) * G(n-i) - (1)

            G(n)=∑    F(i,n)  - (2) If we do this for each i in the array we have our result
              i=1 to n

            From (1) and (2)

            G(n)=∑      G(i−1)   *   G(n−i)
            i=1 to n
            This is a repeating sub-problem and hence has a dp solution
        '''
        G = [0]*(N+1)
        G[0], G[1] = 1, 1

        for n in range(2, N+1):
            for j in range(1, n+1):
                G[n] += G[j-1] * G[n-j]
        return G[N]
        

s = Solution()
print(s.numTrees(4))
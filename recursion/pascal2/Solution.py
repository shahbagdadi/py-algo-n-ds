from typing import List

class Solution:
   
    def tri(self, n , max, l ):
        if n == max :
            return l
        r =[1]
        for i in range(1,len(l)) :
            r.append(l[i-1]+l[i])
        r.append(1)
        return self.tri(n+1,max,r)
    

    def getRowR(self, rowIndex: int) -> List[int]:
        """ Recursive Solution """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [ 1, 1]
        return self.tri(2,rowIndex+1,[1,1])

    def getRow(self, rowIndex: int) -> List[int]:
        """ 
            T - O(n*n) & S - O(n)
        """
        r = [1] * (rowIndex + 1)
        if (rowIndex > 1) :
            max = 2
            while max <= rowIndex:
                p = r.copy()
                for i in range(1,max):
                    r[i] = p[i] + p[i-1]
                max += 1
        return r

    def getRowO(self, rowIndex):
        """ 
            Compact soultion  => T - O(n*n)  & S - O(n)
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

s = Solution()
print(s.getRowO(4))

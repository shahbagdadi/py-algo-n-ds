

class Solution:
    # https://leetcode.com/problems/reaching-points/discuss/375429/Detailed-explanation.-or-full-through-process-or-Java-100-beat
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx   # short cut to top parent https://leetcode.com/problems/reaching-points/discuss/230588/Easy-to-understand-diagram-and-recursive-solution
        if sx == tx and sy <= ty :
            return (ty - sy) % sx == 0 
        elif sy == ty and sx <= tx :
            return (tx - sx) % sy == 0
        return False


s = Solution()
print(s.reachingPoints(9,10,9,19))
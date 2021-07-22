from typing import List

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dist = [0] * len(dominoes) # store dist of current from last R
        lst = list(dominoes)
        lr = ll = -1
        for i, c in enumerate(dominoes):
            if c == 'R' : lr = i # location of last seen R
            elif c == '.' and lr > -1 : 
                dist[i] = i-lr  # if . then set dist from last R
                lst[i] = 'R'
            else :  # for L reset lr
                lr = -1
        for i in range(len(lst) - 1, -1, -1):
            c = dominoes[i]
            if c == 'L' : ll = i    # location of last seen L
            elif c == '.' and ll > -1 :
                if ll-i == dist[i] : # if ldist == rdist then set to .
                    lst[i] = '.'
                elif ll-i < dist[i] or lst[i] == '.' : 
                    lst[i] = 'L'    # if ldist < rdist set L
            else :
                ll = -1   
        return ''.join(lst)       


s = Solution()
ip = ".L.R...LR..L.."
ans = s.pushDominoes(ip)
print(ans)
from typing import List

class Solution :

 def convertToString(self, A : List[str]) -> str :
    meta_data = ','.join([str(len(s)) for s in A])
    return meta_data + '|' + ''.join(A) 

 def convertBackToArray(self, encoded : str) -> List[str] :
    meta_data , sep , data = encoded.partition('|')
    e = 0
    mdata = [ int(s) for s in meta_data.split(',')]
    e , decoded = 0 , []
    for l in mdata:
        s = e
        e += l
        decoded.append(data[s:e])
    return decoded

s = Solution()
ip = ['hello', 'hi' , '' , 'b|ye']
ans1 = s.convertToString(ip)
print(ans1)
ans2 = s.convertBackToArray(ans1)
print(ans2)
from typing import List

class Solution :

 def convertToString(self, A : List[str]) -> str :
    meta_data = ','.join([str(len(s)) for s in A])
    return meta_data + '|' + ''.join(A) 

 def convertBackToArray(self, encoded : str) -> List[str] :
    meta_data , sep , data = encoded.partition('|')
    if not meta_data : return []
    mdata = [ int(s) for s in meta_data.split(',')]
    s , decoded = 0 , []
    for l in mdata:
        decoded.append(data[s:s+l])
        s += l
    return decoded

s = Solution()
ip = ['hel,lo', 'hi' , '' , 'b|ye']
ans1 = s.convertToString(ip)
print(ans1)
ans2 = s.convertBackToArray(ans1)
print(ans2)
from typing import List

class Solution :
 def convertToString(self, A : List[str]) -> str :
    meta_data = ','.join([str(len(s)) for s in A])
    return meta_data + '|' + ''.join(A) 

 def convertBackToArray(self, encoded : str) -> List[str] :
    meta_data , sep , data = encoded.partition('|')
    if not meta_data : return []
    s , decoded = 0 , []
    for l in meta_data.split(',') :
        i = int(l)
        decoded.append(data[s:s+i])
        s += i
    return decoded

s = Solution()
ip = ['hel,lo', 'hi' , '' , 'b|ye']
ans1 = s.convertToString(ip)
print(ans1)
print(s.convertBackToArray(ans1))
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m ,n , z = len(num1) , len(num2), ord('0')
        pos = [0] * (m + n)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = (ord(num1[i]) - z) * (ord(num2[j]) - z)
                p1 , p2 = i+j , i+j+1
                sm = mul + pos[p2]
                pos[p1] += sm // 10
                pos[p2] = sm % 10
        pt = 0
        while pt < len(pos) and pos[pt] == 0:
            pt += 1
        return '0' if pt == len(pos) else ''.join(str(x) for x in pos[pt:])
        

s = Solution()
ans = s.multiply('123', '456')
print(ans)
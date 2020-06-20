import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def isIPv6(s) :
            try:
                return len(s) <= 4 and int(s,16) >= 0
            except:
                return False

        if IP.count('.') == 3 and all(isIPv4(s) for s in IP.split('.')) : return 'IPv4'
        if IP.count(':') == 7 and all(isIPv6(s) for s in IP.split(':')) : return 'IPv6'
        return 'Neither'
        
        
    def validIPAddressR(self, IP: str) -> str:
        ipv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        r_ipv4 = re.compile(r'^(' + ipv4 + r'\.){3}' + ipv4 + r'$')

        ipv6 = r'([0-9a-fA-F]{1,4})'
        r_ipv6 = re.compile(r'^(' + ipv6 + r'\:){7}' + ipv6 + r'$')

        if r_ipv4.match(IP) : return 'IPv4'
        if r_ipv6.match(IP) : return 'IPv6'
        return 'Neither'



s = Solution()
# valid = s.validIPAddress
valid = s.validIPAddressR
ip = "172.16.254.1"
ans = valid(ip)
print(ans)

ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"
ans = valid(ip)
print(ans)

ip = "256.256.256.256"
ans = valid(ip)
print(ans)

ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ans = valid(ip)
print(ans)

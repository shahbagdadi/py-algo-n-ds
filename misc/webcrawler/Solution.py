# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import concurrent.futures
class Solution:
    def getHostname(self, url: str):
        # assume URLs are valid
        return url.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        s = set()
        s.add(startUrl)
        hostname = self.getHostname(startUrl)
        queue = [startUrl]
        while len(queue) > 0:
            queue2 = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                url_iters = list(executor.map(lambda url: htmlParser.getUrls(url), queue))
                for urls in url_iters:
                    for newUrl in urls:
                        if newUrl in s or self.getHostname(newUrl) != hostname:
                            continue
                        s.add(newUrl)
                        queue2.append(newUrl)
            queue = queue2
        return list(s)
        
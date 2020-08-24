from typing import List
from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque()
        self.maxLen = max(map(len, words))
        for word in words:
            node = self.trie
            for c in word[::-1] :
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True


    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        if len(self.stream) > self.maxLen :
            self.stream.pop()
        node = self.trie
        for c in self.stream:
            if  '$' in node :
                return True
            elif c not in node :
                return False
            node = node[c]
        return '$' in node
        

ip = ["cd","f","kl"]
s = StreamChecker(ip)
print(s.query('a'))
print(s.query('c'))
print(s.query('d'))
print(s.query('b'))
print(s.query('f'))
print(s.query('k'))
print(s.query('l'))
print(s.query('e'))
print(len(s.stream))
from typing import List
import collections
import sys

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.sum = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.kmap = {}
        

    def insert(self, key: str, val: int) -> None:
        current , pval = self.root, 0
        if key in self.kmap : pval = self.kmap[key]
        self.kmap[key] = val
        val -= pval
        for letter in key:
            current = current.children[letter]
            current.sum += val

    def sum(self, prefix: str) -> int:
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None: return 0
        return current.sum


# Your MapSum object will be instantiated and called as such:
ms = MapSum()
ms.insert("apple",3)
print(ms.sum("ap"))
ms.insert("app",2)
print(ms.sum("ap"))
ms.insert("apple",2)
print(ms.sum("ap"))
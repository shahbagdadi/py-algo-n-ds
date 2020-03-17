from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0: return []
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]
        return generate(1, n)

s = Solution()
ans = s.generateTrees(3)
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , serialize
for tree in ans:
    try:
        print(serialize(tree))
        drawtree(tree)
    except:
        pass

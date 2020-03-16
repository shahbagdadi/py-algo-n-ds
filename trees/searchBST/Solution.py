# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        else :
            return root

import sys
import os
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize
root = deserialize('[4,2,7,1,3,null,null]')
# drawtree(root)

s = Solution()
r = s.searchBST(root,2)
drawtree(r)

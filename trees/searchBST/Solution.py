# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        elif root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

s = Solution()

import sys
import os
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize
root = deserialize('[4,2,7,1,3,null,null]')
# drawtree(root)

r = s.searchBST(root,2)
drawtree(r)

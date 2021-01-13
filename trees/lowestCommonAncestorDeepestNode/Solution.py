from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root) :
            if not root : return 0,None
            hl, lca = helper(root.left)
            hr, rca = helper(root.right)
            if hl > hr : return hl+1,lca
            if hr > hl : return hr+1, rca
            return hl+1, root
        return helper(root)[1]


import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
# drawtree(root)

s = Solution()
ans = s.lcaDeepestLeaves(root)
drawtree(ans)

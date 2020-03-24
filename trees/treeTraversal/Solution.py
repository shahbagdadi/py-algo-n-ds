from typing import List
import sys , os
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize , serialize

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse(self, root: TreeNode) -> List[int]:
        ans , stk , p = [], [], root
        while stk or p :
            if p :
                stk.append(p)
                # ans.append(p.val)       # Preorder - Add parent to end of list before child
                p = p.left                # Preorder & InOrder
                # ans.insert(0,p.val)     # PostOrder - Reverse of preorder - append to start of list
                # p = p.right             # PostOrder - Reverse the traversal process of preorder

            else:
                node = stk.pop()
                ans.append(node.val)      # InOrder - Add after all left children
                p = node.right            # Preorder & InOrder
                # p = node.left           # PostOrder - Reverse the traversal process of preorder
        return ans

s = Solution()
root = deserialize('[1,null,2,3]')
# drawtree(root)
print(s.traverse(root))
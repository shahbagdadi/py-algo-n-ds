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

    def inorderMorris(self, root):
            cur = root
            while cur:
                if cur.left:
                    temp = cur.left
                    while temp.right and temp.right != cur: temp = temp.right
                    if not temp.right:
                        temp.right, cur = cur, cur.left
                        continue
                    temp.right = None
                print(cur.val)
                cur = cur.right

s = Solution()
root = deserialize('[5,2,6,null,3,null,7]')
# drawtree(root)
print(s.traverse(root))
s.inorderMorris(root)
drawtree(root)

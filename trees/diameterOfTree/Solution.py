

import sys
import os
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree, deserialize, serialize

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def height(node):
            if not node:
                return 0
            lh, rh = height(node.left),  height(node.right)
            self.ans = max(self.ans, lh + rh)
            # print(lh, rh)
            return max(lh, rh) + 1

        height(root)
        return self.ans


s = Solution()
root = deserialize('[1,2,3,4,5]')
ans = s.diameterOfBinaryTree(root)
print(ans)
# drawtree(root)
# serialize(root)

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if not root : return 0
            left = max(0,helper(root.left))
            right = max(0,helper(root.right))
            self.ans = max(self.ans,root.val + left + right)
            return root.val + max(left, right)     
        self.ans = root.val
        helper(root)
        return self.ans

s = Solution()
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[-10,9,20,null,null,15,7]')
# drawtree(root)
# serialize(root)

ans = s.maxPathSum(root)
print(ans)


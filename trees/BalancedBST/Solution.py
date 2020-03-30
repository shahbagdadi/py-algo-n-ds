
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getHeight(self,root):
        if not root : return -1
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root : return True
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2: return True
        return False


s = Solution()
# root = deserialize('[1,2,2,3,3,null,null,4,4]')
root = deserialize('[1,2,2,3,null,null,3,4,null,null,4]')
print(s.isBalanced(root))
drawtree(root)
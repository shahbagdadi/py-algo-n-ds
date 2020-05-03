
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode: 
        def upsideDown(node, parent, parentRight):
            oldLeft , oldRight = node.left , node.right
            # consider the left child as node
            node.left = parentRight
            node.right = parent

            # if left most with no other children then this is the new root
            if not oldLeft and not oldRight :
                return node

            # tail recusrion Memory - O(1) but not in python :(
            return upsideDown(oldLeft, node, oldRight)

        if not root : return None
        return upsideDown(root, None , None)


import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[1,2,3,4,5]')
# drawtree(root)


s = Solution()
new_root = s.upsideDownBinaryTree(root)
drawtree(new_root)
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:

        def leftBoundary(node):
            if not node or not node.left and not node.right: return
            boundary.append(node.val)
            if node.left :
                leftBoundary(node.left)
            else:
                leftBoundary(node.right)

        def leaves(node):
            if not node : return
            leaves(node.left)
            if node != root and not node.left and not node.right :
                boundary.append(node.val)
            leaves(node.right)
            
        def rightBoundary(node):
            if not node or not node.left and not node.right: return
            if node.right :
                rightBoundary(node.right)
            else:
                rightBoundary(node.left)
            boundary.append(node.val)

        if not root : return []
        boundary = [root.val]
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return boundary


import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
# root = deserialize('[1,2,3,4,5,6,null,null,null,7,8,9,10]')
root = deserialize('[[1,null,4,3,null,2,null,5]')
# drawtree(root)
# serialize(root)
s = Solution()
ans = s.boundaryOfBinaryTree(root)
print(ans)
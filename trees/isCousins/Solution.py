
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res = []
        def traverse(node, parent, depth):
            if not node : return 
            if node.val == x or node.val == y :
                res.append((parent,depth))
            traverse(node.left,node,depth+1)
            traverse(node.right,node,depth+1)
            return 
        traverse(root,None,0)
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]

        


import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[1,2,3,4,null,5,null]')
# root = deserialize('[1,2,3,4,null,5,null]')
# drawtree(root)
# serialize(root)

s = Solution()
ans = s.isCousins(root,2,3)
print(ans)
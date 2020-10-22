from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root : return 0
        q , ncnt , level = deque([root]) , 1 , 1
        while q:
            node = q.popleft()
            ncnt -= 1
            if node.left : q.append(node.left)
            if node.right : q.append(node.right)
            if not (node.left or node.right) : return level 
            if ncnt == 0 :
                level += 1
                ncnt = len(q)
        return level

s = Solution()
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
# root = deserialize('[1,2,3,4,null,null,5]')
root = deserialize('[2,null,3,null,4,null,5,null,6]')
# drawtree(root)
# serialize(root)
ans = s.minDepth(root)
print(ans)
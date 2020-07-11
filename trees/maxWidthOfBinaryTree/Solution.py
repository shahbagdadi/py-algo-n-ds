from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque([(root,0)])
        cnt , ans = 1, 1
        while q :
            node , col = q.popleft()
            cnt -= 1
            if node.left : q.append((node.left, 2 * col))
            if node.right : q.append((node.right, 2 * col+1))
            if cnt == 0:
                cnt = len(q)
                if cnt > 1 :
                    ans = max(ans,q[-1][1]-q[0][1] + 1)
        return ans

import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[1,1,1,1,null,null,1,1,null,null,1]')
# drawtree(root)
# serialize(root)

s = Solution()
ans = s.widthOfBinaryTree(root)
print(ans)
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q , res , cnt = deque() , [] , 1
        if not root : return []
        q.append(root)
        while q:
            n = q.popleft()
            cnt -= 1
            if n.left : q.append(n.left)
            if n.right : q.append(n.right)
            if cnt == 0:
                res.append(n.val)
                cnt = len(q)
                # print(q, cnt)
        return res

import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('1,2,3,null,5,null,4')
# drawtree(root)
# serialize(root)
s = Solution()
ans = s.rightSideView(root)
print(ans)
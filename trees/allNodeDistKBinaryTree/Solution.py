from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        def dfs(node,par=None):
            if node: 
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        q , visited = deque([(target, 0)]) , set([target])
        while q:
            if q[0][1] == K :
                return [node.val for node, d in q]
            node , d = q.popleft()
            print(node)
            for nei in (node.left , node.right, node.par):
                if nei and nei not in visited :
                    q.append((nei, d + 1))
                    visited.add(nei)
        return []

import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
# drawtree(root)
# serialize(root)

s = Solution()
ans = s.distanceK(root,root.left,2)
print(ans)
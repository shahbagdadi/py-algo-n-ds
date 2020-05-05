from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        hmax , hdict = 0 , defaultdict(list)

        def traverse(node):
            if not root : return 0
            lh , rh = 0,0
            if node.left:
                lh = traverse(node.left)
            if node.right:
                rh = traverse(node.right)
            h = max(lh,rh) + 1
            hdict[h].append(node.val)
            return h

        traverse(root)
        return [ hdict[i] for i in range(1,len(hdict)+1)]

s = Solution()
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[1,2,3,4,5]')
# drawtree(root)
# serialize(root)

ans = s.findLeaves(root)
print(ans)